#!/usr/bin/env python

# 二分查找
# 输入数组和要查找的项, 找到即返回对应的下标
# 找不到则返回None

def binSearch_1(array, item):
   # 检测输入
    pass

    if len(array) == 0:
        return None
    if len(array) == 1:
        if array[0] == item:
            return 0
        else:
            return None
    else:
        mid = int(len(array)/2)
        if item == array[mid]:
            return mid
        if item < array[mid]:
            return binSearch(array[:mid], item)
        else:
            return binSearch(array[mid:], item)
            
def binSearch(array, item):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = int((start+end)/2)
        if array[mid] == item:
            return mid
        elif item < array[mid]:
            end = mid - 1
        elif item > array[mid]:
            start = mid + 1
    return -1 