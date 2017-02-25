#! /usr/bin/env python
# coding=utf-8

def power(x, n=2):
    if not isinstance(x, (int, float)):
        raise TypeError("Error operand!")
    s = 1
    for i in range(n):
        s *= x
    return s

def test_power():
    x = input("请输入数字:")
    if isinstance(x, (int)):
        print("%s is str" % (x))
    print(power(int(x)))

if __name__ == "__main__":
    test_power()