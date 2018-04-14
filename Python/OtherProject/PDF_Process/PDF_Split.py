#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
import getopt
from PyPDF2 import PdfFileWriter, PdfFileReader

def help():
    print("PDF_Split.py -i <inputfile> -o <outputfile>")

def get_opt(sargv):
    infile = ''
    cfgfile = ''
    try:
        opts, args = getopt.getopt(sargv, 'hc:i:', ["cfile=", 'ifile='])
        #print(sargv, opts) #
    except getopt.GetoptError:
        help()
        print('error') #
        sys.exit(2)
    for opt, arg in opts:
        print(opt, arg) #
        if opt == '-h':
            help()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            infile = arg
        elif opt in ("-c", "-cfile"):
            cfgfile = arg
    return cfgfile, infile


def get_outinfo(cfgfile):
    out_dict = dict()
    # cfgfile 内容格式为：outfile,1-5
    with open(cfgfile, 'r') as cfg:
        for line in cfg.readlines():
            outfile, page_range = line.split('|')
            if outfile not in out_dict:
                out_dict[outfile] = page_range.split('-')
    return out_dict

def split_pdf(pdf_file, outfile, start_page, end_page):
    output = PdfFileWriter()
    
    for i in range(start_page, end_page):
        output.addPage(pdf_file.getPage(i))
    
    with open(outfile, 'wb') as ofd:
        output.write(ofd)

def main():
    cfgfile, infile = get_opt(sys.argv[1:])
    print("cfg:%s; infile:%s" % (cfgfile, infile)) #
    out_dict = get_outinfo(cfgfile)

    # 处理pdf信息, strict参数要设为False， 否则会报错
    pdf_file = PdfFileReader(open(infile, 'rb'), strict=False)
    pdf_pages_len = pdf_file.getNumPages()

    for outfile in out_dict.keys():
        start_page = int(out_dict[outfile][0]) - 1
        end_page = int(out_dict[outfile][1])
        
        if end_page > pdf_pages_len:
            raise Exception('endpage larger than pdf_pages_len')
        split_pdf(pdf_file, outfile, start_page, end_page)
    
if __name__ == '__main__':
    print(sys.argv)
    main()