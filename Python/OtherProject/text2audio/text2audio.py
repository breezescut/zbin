#!/usr/bin/env python

def first_one():
    from aip import AipSpeech

    """ 你的 APPID AK SK """
    APP_ID = '10305374'
    API_KEY = 'kC8mN4U2D0d3iZNrWe75RMBq'
    SECRET_KEY = 'kEnc28nyWat6CP0Kx3r9UEbjGlLkyS0'

    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result  = aipSpeech.synthesis('你好百度', 'zh', 1, {'vol': 5,})

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
    else:
        print(result)


from aip import AipSpeech
import codecs
import chardet

class audio2text:
    def _init(self, infile, outfile):
        self.APP_ID = '10305374'
        self.API_KEY = 'kC8mN4U2D0d3iZNrWe75RMBq'
        self.SECRET_KEY = 'kEnc28nyWat6CP0Kx3r9UEbjGlLkyS0'
        self.aipSpeech = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

        self.infile = infile
        self.outfile = outfile
    
    
    def _convert_encoding(self, filename, target_encoding):
        # Backup the origin file.

        # convert file from the source encoding to target encoding
        content = codecs.open(filename, 'r').read()
        source_encoding = chardet.detect(content)['encoding']
        print("encoding:%s" % source_encoding)
        if source_encoding != 'gbk':
            # print source_encoding, filename
            content = content.decode(source_encoding, 'ignore') #.encode(source_encoding)
            codecs.open(filename, 'w', encoding=target_encoding).write(content)


    def _findEncoding(self, s):
        file = open(s, mode='rb')
        buf = file.read()
        result = chardet.detect(buf)
        file.close()
        return result['encoding']


    def _convertEncoding(self, s):
        encoding = self._findEncoding(s)
        if encoding != 'gbk':
            print("convert %s %s to gbk" % (s, encoding))
            contents = ''
            with codecs.open(s, "r", encoding, 'ignore') as sourceFile:
                contents = sourceFile.read()
            with codecs.open(s, "w", "gbk", 'ignore') as targetFile:
                targetFile.write(contents)
        else:
            print("%s encoding is %s ,there is no need to convert" % (s, encoding))

    def _audio2text(self):
        self._convertEncoding(self.infile)
        with open(self.outfile, mode='wb') as outf:
            with open(self.infile, mode='r') as inf:
                while True:
                    chunk = inf.read(1000)
                    if not chunk:
                        break
                    print(chunk)
                    print("-"*80)
                    result  = self.aipSpeech.synthesis(chunk, 'zh', 1, {'vol': 5,})
                    if not isinstance(result, dict):
                        outf.write(result)
                        print("output mp3")
                    else:
                        print("return error" + str(result))
        
    def trans(self, infile, outfile):
        self._init(infile, outfile)
        self._audio2text()

if __name__ == '__main__':
    aut = audio2text()
    infile = input("输入文本的路径：")
    outfile = input("输出文件路径：")
    aut.trans(infile, outfile)
