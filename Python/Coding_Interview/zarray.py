#! /usr/bin/env python

# 编写 zarray  的练习代码, 自建一个 zarray 类, 可支持多种接口调用
# zarray1 类内部使用 python 自带的 list 进行数据存储, 但所有接口都是另外编写
# 不采用 list 已有的接口, 如 append 等. 还要编写单元测试函数, 测试比较 zarray和list 各自接口的性能

# zarray2 内部采用 C 写的接口, 外面再包装 Python 的调用接口, 同样比较与 list 之间的调用差异

from collections import Iterable

class ArrError(Exception):
    def __init__(self, err_info):
        self.__err = err_info
    
    def info(self):
        return self.__err

class Zarray1(object):
    def __init__(self, arr=None, capacity=10):
        if capacity < 0:
            raise ArrError("Capacity init value can't less than zero")
        if not isinstance(capacity, int):
            raise ArrError("Capacity only support int type")
        if arr == None:
            self.__capacity = capacity
            self.__arr =[None] *  self.__capacity
            self.__size = 0
        else:
            if not isinstance(arr, (list, tuple, str)):
                raise ArrError("arr type error")
            self.__size = len(arr)
            self.__capacity = self.__size * 2
            self.__arr = [None] * self.__capacity
            for i in range(len(arr)):
                self.__arr[i] = arr[i]
    
    def size(self):
        return self.__size

    def capacity(self):
        return self.__capacity
    
    def is_empty(self):
        if self.__size == 0:
            return True
    
    def at(self, index):
        if index >= self.__size:
            raise ArrError("Out of the range") 
        return self.__arr[index]

    def push(self, item):
        self.__check_item(item)
        if self.__size == self.__capacity:
            if self.__capacity == 0:
                self.__capacity = 1
            self.__resize(self.__capacity*2)
        self.__arr[self.__size] = item
        self.__size += 1
    
    def insert(self, index, item):
        self.__check_item(item)
        if index == self.__size:
            self.push(item)
        if self.__size == self.__capacity:
            self.__resize(self.__capacity*2)
        for i in range(self.__size - 1, index - 1, -1):
            self.__arr[i+1] = self.__arr[i]
        self.__size += 1
        self.__arr[index] = item
            
    def prepend(self, item):
        self.__check_item(item)
        self.insert(0, item)
    
    def pop(self):
        self.__arr[self.__size-1] = None
        self.__size -= 1
        if self.__size <= self.__capacity/4:
            self.__resize(self.__capacity/2)
    
    def delete(self, index):
        for i in range(index, self.__size, 1):
            self.__arr[i] = self.__arr[i+1]
        self.__arr[self.__size-1] = None
        self.__size -= 1
        if self.__size <= self.__capacity/4:
            self.__resize(self.__capacity/2)

    def remove(self, item):
        indexs = []
        for i in range(self.__size):
            if self.__arr[i] == item:
                indexs.append(i)
                self.delete(i)
        return indexs
    
    def find(self, item):
        self.__check_item(item)
        for i in range(self.__size):
            if self.__arr[i] == item:
                return i 
        raise ArrError("Not find the item")
    
    def __resize(self, new_capacity):
        new_arr = [None] * new_capacity
        old_arr = self.__arr
        for i in range(self.__size):
            new_arr[i] = self.__arr[i]
        self.__arr = new_arr
        self.__capacity = new_capacity
        for i in range(len(old_arr)):
            old_arr[i] = None

    def __check_item(self, item):
        if not isinstance(item, (int, bool, str, float)):
            raise ArrError("Not a verified type")
        
