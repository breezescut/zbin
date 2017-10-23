#! /usr/bin/env python

import sys
import xlrd
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

## open the excel file
def open_excel(xfile):
    xdata = xlrd.open_workbook(xfile)
    return xdata

## create the template of the mail
def create_template():
    ori_template = '''
        <table tabindex="65535" class="xdLayout" style="word-wrap: break-word; border-top: medium none; border-right: medium none; width: 700px; border-collapse: collapse; table-layout: fixed; border-bottom: medium none; border-left: medium none"
        bordercolor="#ffffff" border="1">
            <tbody>
                <tr style="min-height: 25px">
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
            </tbody>
        </table>
    '''
    return ori_template

def create_msg(xtemplate, xtitles, xvalues):
    print(xtemplate, xtitles, xvalues)
    print(tuple(xtitles+xvalues))
    msg = xtemplate % tuple(xtitles+xvalues)
    print(msg)
    return msg

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(server, from_addr, to_addr, to_name, xmsg):
    msg = MIMEText(xmsg, 'html', 'utf-8')
    # msg = MIMEText("hello", 'plain', 'utf-8')
    msg['From'] = _format_addr('李晓英<%s>' % from_addr)
    msg['To'] = _format_addr('%s<%s>' % (to_name, to_addr))
    msg['Subject'] = Header('你的工资条', 'utf-8').encode()
    server.sendmail(from_addr, to_addr, msg.as_string())

def get_cell_value(xvalue):
    new_value = str(xvalue).split(sep=':')[1]
    if new_value.find("\'") != -1:
        new_value = new_value.split(sep='\'')[1]
    return new_value


def main():
    print(sys.argv)
    sys.argv.append(r"d:\Temp\xx.xlsx")
    print(sys.argv)


    to_addr_index = 10
    to_name_index = 1

    from_addr = "zhengjinbin@utrust.cn"
    mail_pass = ""
    smtp_server = "smtp.utrust.cn"
    # from_addr = "breezescut@163.com"
    # mail_pass = input("请输入邮箱密码：")
    # smtp_server = "smtp.163.com"
    
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    print("from_addr:%s;mail_pass:%s" % (from_addr, mail_pass))
    server.login(from_addr, mail_pass)

    print("Debug:login")

    value_indexs = [1,2,3,4,5,6,7,8,9]
    xtemplate = create_template()
    
    xdata = open_excel(sys.argv[1])
    xtable = xdata.sheet_by_index(0)
    titles = []
    for icol in value_indexs:
        titles.append(get_cell_value(xtable.row(0)[icol]))
    
    values = []
    for irow in range(1, xtable.nrows):
        to_addr = get_cell_value(xtable.row(irow)[to_addr_index])
        to_name = get_cell_value(xtable.row(irow)[to_name_index])

        for icol in value_indexs:
            values.append(get_cell_value(xtable.row(irow)[icol]))    
        msg = create_msg(xtemplate, titles, values)
        send_mail(server, from_addr, to_addr, to_name, msg)

if __name__ == "__main__":
    main()
