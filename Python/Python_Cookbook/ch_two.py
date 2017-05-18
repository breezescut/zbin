#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest

class TestChTwo(unittest.TestCase):
    # 2.1 使用多个界定符分割字符串
    def n_test_2_1(self):
        # 一个界定符的情况
        p1 = 'asd,asdsa,sadsa,d,sa,dsa,d,sa,dsa'
        p_list = p1.split(',')
        print(p_list)

        # 多个界定符的情况
        import re
        p2 = 'asdf fjdk; afed, fjek,asdf, foo'
        p_list2 = re.split(r'[;,\s]\s*', p2)
        print(p_list2)

        # 捕获界定符
        #p_list3 = re.split(r'(;|,|\s)\s*', p2)
        p_list3 = re.split(r'([;,\s])\s*', p2)
        words = p_list3[::2]
        dilimiters = p_list3[1::2] + ['']
        print(words)
        print(dilimiters)
        print(''.join(v+d for v, d in zip(words, dilimiters)))
    
    # 2.2 字符串开头或结尾匹配
    def n_test_2_2(self):
        filenames = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
        fs = [name for name in filenames if name.endswith(('c', 'py', 'h'))]
        print(fs)

    # 2.3 用 Shell 通配符匹配字符串
    def n_test_2_3(self):
        from fnmatch import fnmatch, fnmatchcase

        names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']

        print([name for name in names if fnmatch(name, '*csv')])
    
    # 2.5 字符串搜索和替换
    def test_2_5(self):
        text1 = 'yeah, but no, but yeah, but no, but yeah'
        text1 = text1.replace('yeah', 'yes')
        print(text1)

        import re
        text2 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
        #text2 = re.sub(r'(\d+)/(\d+)/(\d+)', '\3-\1-\2', text2)
        # 匹配模式不加 r'' 会导致乱码
        text3 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text2)
        print(text3)

        datapat = re.compile(r'(\d+)/(\d+)/(\d+)')
        text4 = datapat.sub(r'\3-\1-\2', text2)
        print(text4)


        