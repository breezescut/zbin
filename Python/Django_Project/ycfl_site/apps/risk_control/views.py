from django.shortcuts import render

import os
import datetime
from ftplib import FTP

month = '' + str(datetime.datetime.now().year) + str(datetime.datetime.now().month)

class mdata():

    def __init__(self):
        self.index_list = [
            'provision_rate', 'reject_ratio', 'recovery_rate', 'vendor_leasing', 'single_holder_cor',
            'single_group_cen',
            'single_customer_cor', 'single_customer_cen', 'aum', 'rate_risk', 'liq_ratio', 'total_cor',
            'after_sale_rent',
            'loss_ratio', 'interbank_ratio', 'overdue_rate', 'direct_rental', 'capital_adequacy_ratio',
            'income_growth_rate',
            'profit_increase_rate', 'roe']
        self.index_dict = {
            'provision_rate': ['拨备率', '%'],
            'reject_ratio': ['不良率', '%'],
            'recovery_rate': ['不良资产处置回收率', '%'],
            'vendor_leasing': ['厂商租赁业务', '%'],
            'single_holder_cor': ['单一股东关联度', '%'],
            'single_group_cen': ['单一集团客户集中度', '%'],
            'single_customer_cor': ['单一客户关联度', '%'],
            'single_customer_cen': ['单一客户集中度', '%'],
            'aum': ['管理资产规模', '万元'],
            'rate_risk': ['利率风险', '%'],
            'liq_ratio': ['流动比率', '%'],
            'total_cor': ['全部关联度', '%'],
            'after_sale_rent': ['售后回租业务', '万元'],
            'loss_ratio': ['损失率', '%'],
            'interbank_ratio': ['同业拆借比例', '%'],
            'overdue_rate': ['逾期率', '%'],
            'direct_rental': ['直租业务', '万元'],
            'capital_adequacy_ratio': ['资本充足率', '%'],
            'income_growth_rate': ['收入增长率', '%'],
            'profit_increase_rate': ['利润增长率', '%'],
            'roe': ['净资产收益率', '%'],
        }

    def get_index_list(self):
        return self.index_list

    def get_index_dict(self):
        return self.index_dict

    def dict_items(self):
        for x, y in self.index_dict.items():
            y1, y2 = y
            yield x, y1, y2

mydata = mdata()

# Create your views here.
def index(request):
    context = {
        'month': month,
        'index_dict': mydata,
               }
    return render(request, 'risk_control/index.html', context)

def submit(request):
    ser = 1
    submit_context = ''
    index_dict = mydata.get_index_dict()
    for idx in mydata.get_index_list():
        idx_value = request.POST[idx] if request.POST[idx] else str(0.00)
        idx_value = idx_value + index_dict[idx][1]
        istr = '|'.join([str(ser), index_dict[idx][0], month, idx_value ]) + '\n'
        submit_context += istr
        ser += 1
    
    out_file = 'data/output/' + 'jz_riskj_' + month + '.txt'
    with open(out_file, 'w', encoding='utf8') as f:
        f.write(submit_context)

    
    context = {'submit_context': submit_context.split(sep='\n')}
    # ftp 到 指定服务器
    context['result'] = mftp(out_file)
    return render(request, 'risk_control/submit.html', context=context)

def mftp(ffile):
    ftp = FTP('100.100.0.80')
    ftp.login('ftpuser', 'ftpuser')
    bufsize = 1024
    with open(ffile, 'rb') as file_handler:
        ftp.storbinary('STOR %s' % os.path.basename(ffile), file_handler, bufsize)
    ftp.quit()
    return 'File upload ok!'
