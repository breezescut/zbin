#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sys
import getopt
from PyPDF2 import PdfFileWriter, PdfFileReader

def help():
    print("PDF_Process.py -c <configfile>")

def get_opt(sargv):
    infile = ''
    cfgfile = ''
    try:
        opts, args = getopt.getopt(sargv, 'hc:', ["cfile=",])
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
        elif opt in ("-c", "-cfile"):
            cfgfile = arg
    return cfgfile


def get_info(cfgfile):
    out_dict = dict()
    # cfgfile 内容格式为：outfile|infile1@1-5,7,8-9|infile2@1-2,3,7|...|infileN@1-19|
    with open(cfgfile, 'r') as cfg:
        for line in cfg.readlines():
            if line[0] == '#': continue
            outfile, *infiles = line.split('|')
            if infiles[-1] == '' or infiles[-1] == '\n':
                infiles.pop(-1)
            print(infiles)
            out_dict[outfile] = dict()
            for infile in infiles:
                print('infile:%s'% infile)
                fname, page_range = infile.split('@')
                out_dict[outfile][fname] = []
                for page in page_range.split(','):
                    if '-' not in page:
                        out_dict[outfile][fname].append(int(page))
                    elif page == '-':
                        out_dict[outfile][fname].append(page)
                    else:
                        start, end = page.split('-')
                        out_dict[outfile][fname] = out_dict[outfile][fname] + list(range(int(start), int(end)+1))
    return out_dict 

def process_pdf(out_dict):
    for ofile in out_dict.keys():
        odict = out_dict[ofile]
        output = PdfFileWriter()
        for ifile in odict.keys():
            # 处理pdf信息, strict参数要设为False， 否则会报错
            pdf_infile = PdfFileReader(open(ifile, 'rb'), strict=False)
            pdf_pages_len = pdf_infile.getNumPages()
            if odict[ifile][0] == '-':
                odict[ifile] == range(1, pdf_pages_len+1)
            for i in odict[ifile]:
                output.addPage(pdf_infile.getPage(i))
        with open(ofile, 'wb') as ofd:
            output.write(ofd)

def main():
    cfgfile = get_opt(sys.argv[1:])
    print("cfg:%s" % (cfgfile)) #
    out_dict = get_info(cfgfile)
    process_pdf(out_dict)

if __name__ == '__main__':
    print(sys.argv)
    main()