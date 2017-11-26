#!/usr/bin/env python

# https://github.com/MashiMaroLjc/pylimit

import unittest
from type_limit import type_limit

@type_limit(*[int, int], res=int)
def calOne(x, y):
    return x+y

@type_limit(*[int, int], res1=int, res2=int)
def calTwo(x, y):
    return x+y, x-y

class CalThree(object):
    @type_limit(*[object, int, str], res1=int, res2=int, res3=str)
    def calthree(self, x, z):
        y = int(z)
        return x+y, x-y, str(x*y)

class TestTypeLimit(unittest.TestCase):
    # def testOne(self):
    #     calOne(1,2)

    # def testTwo(self):
    #     calTwo(1,2)
    
    def testThree(self):
        CalThree().calthree(1,'2')


if __name__ == '__main__':
    unittest.main()