 # -*- coding: UTF-8 -*- 
import httplib,urllib
import time,json

api_dict = {
    "交易日历数据": "p_public0001",
    "行业分类数据"："p_public0002",
    "地区分类数据": "p_public0003",
    "证券类别编码数据": "p_public0005",
    "公共编码数据": "p_public0006",
    "人民币汇率中间价": "p_public0007",
}

def gettoken(client_id,client_secret):
    url='http://webapi.cninfo.com.cn/api-cloud-platform/oauth2/token' #api.before.com需要根据具体访问域名修改
    post_data="grant_type=client_credentials&client_id=%s&client_secret=%s"%(client_id,client_secret)
    req = urllib.urlopen(url, post_data)
    responsecontent = req.read()
    responsedict=json.loads(responsecontent)
    token=responsedict["access_token"]
    return token

def apiget(scode,tokent):
    url = "http://apitest2.com/api/stock/p_stock2100?scode=%s&access_token=%s" #apitest2.com需要根据具体访问域名修改
    conn = httplib.HTTPConnection("apitest2.com")
    conn.request(method="GET",url=url%(scode,tokent))
    response = conn.getresponse()
    rescontent= response.read()
    responsedict=json.loads(rescontent)
    resultcode=responsedict["resultcode"]
    print responsedict["resultmsg"],responsedict["resultcode"]
    if(responsedict["resultmsg"]=="success" and len(responsedict["records"])>=1):
        print responsedict["records"]  #接收到的具体数据内容
    else:
        print 'no data'
    return resultcode

def apipost(scode,tokent):
    url = "http://apitest2.com/api/stock/p_stock2100"  #apitest2.com需要根据具体访问域名修改
    post_data="scode=%s&access_token=%s"%(scode,tokent)
    req = urllib.urlopen(url, post_data)
    content = req.read()
    responsedict=json.loads(content)
    resultcode=responsedict["resultcode"]    
    print responsedict["resultmsg"],responsedict["resultcode"]
    if(responsedict["resultmsg"]=="success" and len(responsedict["records"])>=1):
        print responsedict["records"]  #接收到的具体数据内容
    else:
        print 'no data'
    return resultcode
       

if __name__=="__main__":
    client_id,client_secret="100001","c4c7de76a9364a37ba3885232345bddc" #client_id,client_secret通过我的凭证获取
    token=gettoken(client_id,client_secret)
    for i in range(0,3600): #注：3600为循环访问API的次数
        scode=str(300000+i) #股票代码，根据自己需要传入
        #resultcode=apiget(scode,token)   #以http get方法获取数据
        resultcode=apipost(scode,token) #以http post方法获取数据
        if resultcode==405: #token失效，重新获取
            token=gettoken(client_id,client_secret)
            apiget(scode,token)  #get请求
            #apipost(scode,token)#post请求
        time.sleep(1)
