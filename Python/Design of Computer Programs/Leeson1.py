#! /usr/bin/env python
# coding=utf-8

def ss(num):
    total = 0
    for i in range(num+1):
        total += i
        #print("%d:%d" % (i, total))
    return total

def poker(hands):
    return max(hands)

def hand_rank(hand):
    

if __name__ == "__main__":
    num = int(input("Input num:"))
    print("sum(%d) = %d" % (num,ss(num)))