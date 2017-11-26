#!/usr/bin/env python

import unittest

from binSearch import binSearch

class Test_BinSearch(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
#    def test_binSearch1(self):
#        # array = [1,2,3,4,5,6,7,8,9]
#        array = sorted('asdfghjklzxcvbnv')
#        b = array[:]
#        b.reverse()
#        for i in b:
#            index = binSearch(array, i)
#            print("item:%s; index:%d\n" % (i, index))

    def test_binSearch(self):
        array = sorted("abcdfghjklnsvxz")
        self.assertEqual(binSearch(array, 'a'), 0)
        self.assertEqual(binSearch(array, 'f'), 4)
        self.assertEqual(binSearch(array, 'z'), len(array) - 1)
        self.assertEqual(binSearch(array, '1'), -1)
        self.assertEqual(binSearch(array, 'as'), -1)

        array = []
        self.assertEqual(binSearch(array, 'a'), -1)

        array = 'a'
        self.assertEqual(binSearch(array, 'a'), 0)
        self.assertEqual(binSearch(array, 'b'), -1)

if __name__ == '__main__':
    unittest.main()