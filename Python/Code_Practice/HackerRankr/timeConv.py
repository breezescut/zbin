#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    flag = s[-2:]
    ptime = s[:-2]
    ntime = ''
    hrs = int(ptime[:2])
    if flag == 'AM':
      if hrs == 12:
        ntime = '00%s' % (ptime[2:])
      else:
        hrs += 12
        ntime = ptime
    elif flag == 'PM':
      ntime = '%d%s' % (hrs, ptime[2:])
    return ntime
      

s = input().strip()
result = timeConversion(s)
print(result)

