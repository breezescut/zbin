#! /usr/bin/env python

import sys
import random
import string
import getopt
import xlwings as xw
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

global_cfg = {
    "user_cfg": "user.xls",
    "to_addr_index": 5,
    "to_name_index": 6,
    "from_addr": "ycjrzl@utrust.cn",
    "mail_pass": "Yc888888",
    "smtp_server": "smtp.utrust.cn",

}

# 生成随机密码
def gen_rand_password(nums):
    passwords = []
    for i in range(nums):
        salt = ''.join(random.sample(string.ascii_letters +string.digits, 8))
        passwords.append(salt)
    return passwords

## open the excel file
def open_excel(xfile):
    wb = xw.Book(xfile)
    return wb

# 填充随机密码到NAS账号配置文件
def fill_paaswd2cfg(wb, passwords):
    sht = wb.sheets.active
    sht.range("B1").options(transpose=True).value = passwords
    wb.save()
    wb.close()

# 初始化smtp server
def init_smtp():
    to_addr_index = global_cfg["to_addr_index"]
    to_name_index = global_cfg["to_name_index"]

    from_addr = global_cfg["from_addr"]
    mail_pass = global_cfg["mail_pass"]
    smtp_server = global_cfg["smtp_server"]
    
    server = smtplib.SMTP(smtp_server, 25)
    # server.set_debuglevel(1)
    print("from_addr:%s;mail_pass:%s" % (from_addr, mail_pass))
    server.login(from_addr, mail_pass)
    return server

## create the template of the mail
def create_template():
    ori_template = '''
        <table tabindex="65535" class="xdLayout" style="word-wrap: break-word; border-top: medium none; border-right: medium none; width: 700px; border-collapse: collapse; table-layout: fixed; border-bottom: medium none; border-left: medium none"
        bordercolor="#ffffff" border="1">
            <tbody>
                <tr style="min-height: 25px">
                    <td>账号</td>
                    <td>密码</td>
                </tr>
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
            </tbody>
        </table>
    '''
    return ori_template

def create_msg(xtemplate, xaccount, xpassword):
    msg = xtemplate % (xaccount, xpassword)
    # print(msg)
    return msg

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(server, from_addr, to_addr, to_name, xmsg):
    msg = MIMEText(xmsg, 'html', 'utf-8')
    # msg = MIMEText("hello", 'plain', 'utf-8')
    msg['From'] = _format_addr('粤财金融租赁<%s>' % from_addr)
    msg['To'] = _format_addr('%s<%s>' % (to_name, to_addr))
    msg['Subject'] = Header('YCFL-NAS 账号密码', 'utf-8').encode()
    server.sendmail(from_addr, to_addr, msg.as_string())

def proc_passwd():
    passwords = gen_rand_password(42)
    wb = open_excel(global_cfg['user_cfg'])
    fill_paaswd2cfg(wb, passwords)
    

def proc_email():
    server = init_smtp()
    wb = open_excel(global_cfg['user_cfg'])
    sht = wb.sheets.active
    to_addrs = sht.range("E1:E42").options(transpose=True).value
    to_names = sht.range("F1:F42").options(transpose=True).value
    
    accounts = sht.range("A1:A42").options(transpose=True).value
    passwords = sht.range("B1:B42").options(transpose=True).value

    xtemplate = create_template()
    to_addrs = [x for x in to_addrs if x != None]
    for idx in range(len(to_addrs)):
        msg = create_msg(xtemplate, accounts[idx], passwords[idx]) 
        print(to_addrs[idx], msg)
        send_mail(server, global_cfg["from_addr"], to_addrs[idx], to_names[idx], msg)   

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sargv, 'ep')
        #print(sargv, opts) #
    except getopt.GetoptError:
        print('error') #
        sys.exit(2)
    for opt, arg in opts:
        print(opt, arg) #
        if opt == '-e':
            proc_email()
        elif opt == '-p':
            proc_passwd()
