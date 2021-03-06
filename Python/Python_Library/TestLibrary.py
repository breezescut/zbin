#!/usr/bin/env python

import unittest

class TestLibrary(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def n_test_setattr(self):
        '''
         利用 setAttr 可以动态增加对象的属性
        '''
        class A():
            a = 1
            b = 1
            def func1(self):
                print('func1')
        
        a = A()
        setattr(A, 'd', "hahhahaha")
        print(a.d)

        from collections import namedtuple
        DD = namedtuple('DD', ['a', 'b', 'c', 'd'])
        dd1 = DD(1,2,3,4)
        print(dd1)
        setattr(DD, 'e', 5)
        print(dd1.e)
    
    def test_list(self):
        fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

        self.assertEqual(fruits.index('apple'), 1)
        self.assertEqual(fruits.count('apple'), 2)

        self.assertEqual(fruits.pop(2), 'pear')

        temp = sorted(fruits)
        fruits.sort()
        self.assertEqual(fruits, temp)

if __name__ == '__main__':
    unittest.main()


