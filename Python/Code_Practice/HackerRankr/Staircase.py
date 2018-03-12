#!/bin/python3

import sys

def staircase(n):
    # Complete this function
    lst = list(' ' * n)
    llst = []
    for i in range(-1, -(n+1), -1):
      lst[i] = '#'
      print(lst)
      llst.append(''.join(lst))
    return llst
      

if __name__ == "__main__":
    # n = int(input().strip())
    n = 6
    print(staircase(n))
    