#!/usr/bin/env python

import os
import re
import bs4
import requests

img_base_url = "http://p1.xiaoshidi.net"
base_dir = r'd:\\WorkHome\\CodeHome\\Python\\Spider\\comic\\data\\'

# get topic url
def get_topic_url(start_url):
    resp = requests.get(start_url)
    soap = bs4.BeautifulSoup(resp.text)
    a_list = soap.select('a')
    a_list = [al for al in a_list if 'title' in al.attrs and 'data-cmd' not in al.attrs]
    # topic_urls : topic:url
    topic_urls = [ '%s||%s/%s' % (t.attrs['title'], start_url, t.attrs['href']) for t in a_list]
    return topic_urls


# get topic sub url
def get_topic_sub_url(topic_url):
    sub_urls = []
    nurl = topic_url
    num = 1
    while True:
        sub_urls.append(nurl)
        print('Debug:%s...' % nurl)
        resp = requests.get(nurl)
        soap = bs4.BeautifulSoup(resp.text)
        divs = soap.select('div')
        div = [d for d in divs if 'class' in d.attrs and d.attrs['class'] == ['navigation']]
        if nurl == 'http://manhua.fzdm.com/25/155//index_25.html':
            pass
        flag = div[0].contents[-1]
        if isinstance(flag, str):
            break
        elif flag.text == '下一话吧':
            break
        else:
            nurl = '%s/index_%d.html' % (topic_url, num)
            num += 1
    return sub_urls

# get all img url
def get_img_urls(sub_url):
    resp = requests.get(sub_url)
    soap = bs4.BeautifulSoup(resp.text)
    sc_list = soap.select('script')
    sc_text = sc_list[10].text
    mhurl = sc_text.split('\n')[2].split('"')[1]
    img_url = '%s/%s' % (img_base_url, mhurl)
    return img_url
    

# download picture
def download_pic(pic_url, target_path):
    resp = requests.get(pic_url)
    fn = '%s\\%s\\%s' % (base_dir, target_path, pic_url.split('/')[-1])
    if os.path.exists(fn) == False:
        with open(fn, 'wb') as fd:
            fd.write(resp.content)
    
if __name__ == '__main__' :
    start_url = 'http://manhua.fzdm.com/25'   # 大剑
    topic_urls = get_topic_url(start_url)
    dirs = [ i.split('||')[0] for i in topic_urls]
    for dir in dirs:
        dir = r'%s\\%s' % (base_dir, dir)
        if os.path.exists(dir) != True:
            os.mkdir(dir)

    for item in topic_urls:
        items = item.split('||')
        target_path = items[0]
        url = items[1]
        print("topic %s processing..." % url)
        topic_sub_urls = get_topic_sub_url(url)
        for sub_url in topic_sub_urls:
            print("sub_topic %s processing..." % sub_url)
            img_url = get_img_urls(sub_url)
            download_pic(img_url, target_path)
    

