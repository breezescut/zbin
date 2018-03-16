import requests
import requests
import random
import hashlib
import json

my_appid = '20180316000136456'
my_key = 'ORyUh6TjPHhLyJwX0nog'
salt = random.randint(0, 100)

def word_classify(context):
    word_dict = dict()
    words = [x.strip() for x in context.split(' ')]
    words = [x.strip(',') for x in words]
    for word in words:
        if word == '':
            continue
        if word in word_dict.keys():
           word_dict[word] += 1
        else:
            word_dict[word] = 1
    for word in word_dict:
        word_dict[word] = "%d|%s" % (word_dict[word], word_translate(word))
    print(word_dict)
    return word_dict

def word_translate(context):
    hl = hashlib.md5()
    string = '%s%s%s%s' % (my_appid, context, salt, my_key)
    hl.update(string.encode(encoding='utf-8'))
    my_sign = hl.hexdigest()
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    data = {
            'q':context,
            'from':'en',
            'to':'zh',
            'appid':my_appid ,
            'salt':salt ,
            'sign':my_sign
        }
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'}
    response = requests.post(url,data,headers=headers)
    head = response.headers
 
    text = response.text
    text = json.loads(text)
    dst = ''
    if 'trans_result' in text.keys():
        dst = text['trans_result'][0]['dst']
    return dst

def test():
    my_dict = {}
    context = 'hello world'
    print('begin classify')
    my_dict = word_classify(context)
    print(my_dict)
    for word in my_dict.keys():
        print(word)
        print("%s: %s" % (word, my_dict[word]))

def main():
    my_dict = {}
    while True:
        context = input('subtitles input(退出q):')
        if context in ['q', 'Q']:
            break
        else:
            print('begin classify')
            my_dict = word_classify(context)
            print(my_dict)
        for word in my_dict.keys():
            print("%s: %s" % (word, my_dict[word]))


if __name__ == '__main__':
    main()
else:
    print('import subtitles_translate sucessed!')