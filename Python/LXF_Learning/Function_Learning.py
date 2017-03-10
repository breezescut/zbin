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

# 可变参数函数定义
# 定义一个学生注册函数
def enroll1(name, sex, age=6, *args):
    print("student info:name=%s, sex=%s, age=%d, other[%s]" %
    ( name, sex, age, str(args)))

def test_enroll1():
    name, sex, age, args = "zbin", "M", 6, (1,2,3,4,5)
    enroll(name, sex, age, 2121,323,442)

# 命名关键字参数
def enroll2(**args):
    print("student info:name=%s, sex=%s, age=%d" %
    ( args['name'], args['sex'], args['age']))

def test_enroll2():
    d = {'name':'zbin', 'age':5, 'sex':'M'}
    enroll2(**d)

# 汉诺塔
def hanoi_1(n, a='A', b='B', c='C'):
    if n == 1:
         print('move', a, '->', c)
         return
    hanoi(n-1, a, c, b)
    print('move', a, '->', c)
    hanoi(n-1, b, a, c)

def test_hanoi_1():
    hanoi(3)

# 测试列表和切片
def test_list_slice():
    li = [1,2,3,4]
    li.append(5)
    print(li)
    li1 = li
    li1.append('b')
    li2 = li.copy()
    li2.append('a')
    li3 = li[:]
    li3.append('c')
    print(li, li1, li2, li3)

    li3.clear()
    print("li3:%s" % li3)

    print("li2 length: %d" % len(li2))
    print("li2 counts:%d" % li2.count(1))
        
    for index, element in enumerate(li):
        print("li[%d]=%s" % (index, element), end=' ') 
    
    print()
    # 切片
    li4 = li1[:2]
    print(li4, end='\n')
    with open(r".\tmp.txt", 'a') as fd:
        print(li4, file=fd)

# 迭代
def test_iterable():
    from collections import Iterable
    import random
    for i in list(range(30)):
        print(i, end=' ')
    print()
    for i in 'hsjhsahd':
        print(i, end=' ')
    print()
    print(isinstance(1, (Iterable)))

    for index, element in enumerate(list(range(random.randint(1,100)))):
        print("list[%d]:%d" % (index, element))

    dict1 = {'name':'zbin', 'age':'30'}
    for x in dict1:
        print(x)
    for x in dict1.items():
        print(x)
    for x in dict1.values():
        print(x)
    iter1 = iter(dict1)
    print(next(iter1))
    print(next(iter1))

def test_listcompr():
    import random
    list1 = list(range(random.randint(1, 10)))
    print(list1)
    print([x*x for x in list1])
    iter1 = (x*x for x in list1)
    
    d = {'x':'a', 'y':'b'}
    list2 = ["%s:%s" % (k, v) for k, v in d.items()]
    print(list2)

    print([ (x+y).lower() for x in 'ABC' for y in 'XYZ' ])

    L = ['Hello', 'WORLD', 18, 'APple', None]
    print([s.lower() for s in L if isinstance(s, str)])

if __name__ == "__main__":
    test_listcompr()