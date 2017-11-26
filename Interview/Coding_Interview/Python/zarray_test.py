#!/usr/bin/env python

# zarry 单元测试

import unittest

from zarray import Zarray1,ArrError

class TestZarry1(unittest.TestCase):

    def setUp(self):
        self.arr = [1,2,3,4,5,6]

    def test_init(self):
        # 空 Case
        arr = Zarray1(capacity=10)
        self.assertEqual(arr._Zarray1__capacity, 10)
        self.assertEqual(arr._Zarray1__size, 0)
        self.assertEqual(arr._Zarray1__arr, [None] * 10)

        # init by list
        arr = Zarray1(self.arr)
        self.assertEqual(arr._Zarray1__capacity, len(self.arr) * 2)
        self.assertEqual(arr._Zarray1__size, len(self.arr))
        self.assertEqual(arr._Zarray1__arr, self.arr + [None] * len(self.arr))

        # init by tuple
        t = (1,2,3,4,5,6)
        arr = Zarray1(t)
        self.assertEqual(arr._Zarray1__capacity, len(t) * 2)
        self.assertEqual(arr._Zarray1__size, len(t))
        self.assertEqual(arr._Zarray1__arr, self.arr + [None] * len(self.arr))

        # init by dict
        d = {'a':1, 'b':2}
        with self.assertRaises(ArrError) as ex:
            arr = Zarray1(d)
        e = ex.exception
        self.assertEqual(e.info(), "arr type error")

        # init by str
        strA = '123456'
        arr = Zarray1(strA)
        self.assertEqual(arr._Zarray1__capacity, len(strA) * 2)
        self.assertEqual(arr._Zarray1__size, len(strA))
        self.assertEqual(arr._Zarray1__arr, list(strA) + [None] * len(strA))

    def test_size(self):
        arr = Zarray1(self.arr)
        self.assertEqual(arr.size(), len(self.arr))

    def test_capacity(self):
        arr = Zarray1(self.arr)
        self.assertEqual(arr.capacity(), len(self.arr) * 2)

    def test_is_empty(self):
        arr = Zarray1()
        self.assertEqual(arr.is_empty(), True)
    
    def test_at1(self):
        arr = Zarray1(self.arr)
        for i in range(arr.size()):
            self.assertEqual(arr.at(i), self.arr[i])
    
    def test_at2(self):
        arr1 = Zarray1()
        with self.assertRaises(ArrError) as ex:
            a = arr1.at(1)
        e = ex.exception
        self.assertEqual(e.info(), "Out of the range")
        
        arr2 = Zarray1(self.arr)
        with self.assertRaises(ArrError) as ex:
            a = arr2.at(arr2.size())
        e = ex.exception
        self.assertEqual(e.info(), "Out of the range")

    def test_push(self):
        # 测试初始化 capacity 为 0 Case
        arr0 = Zarray1(capacity=0)
        self.assertEqual(arr0.size(), 0)
        self.assertEqual(arr0.capacity(), 0)
        arr0.push('a')
        self.assertEqual(arr0.size(), 1)
        self.assertEqual(arr0.capacity(), 2)
        self.assertEqual(arr0.at(0), 'a')

        # 测试初始化 Capacity 为 负数 Case
        with self.assertRaises(ArrError) as ex:
            arr1 = Zarray1(capacity=-10)
        e = ex.exception
        self.assertEqual(e.info(), "Capacity init value can't less than zero")

        # Capacity > 0, arr = None
        arr2 = Zarray1(capacity=10)
        self.assertEqual(arr2.size(), 0)
        self.assertEqual(arr2.capacity(), 10)
        arr2.push('a')
        self.assertEqual(arr2.size(), 1)
        self.assertEqual(arr2.capacity(), 10)
        self.assertEqual(arr2.at(0), 'a')
        for i in '1234567890':
            arr2.push(i)
        self.assertEqual(arr2.size(), 11)
        self.assertEqual(arr2.capacity(), 20)
        self.assertEqual(arr2.at(0), 'a')
        self.assertEqual(arr2.at(9), '9')
    
    def test_insert(self):
        # insert last index
        pass
        
if __name__ == '__main__':
    unittest.main()





    


