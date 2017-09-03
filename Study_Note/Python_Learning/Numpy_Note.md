# Numpy 教程学习笔记
[TutorialsPoint NumPy 教程](http://www.jianshu.com/p/57e3c0a92f3a)

## Numpy - 简介

## Numpy 操作
- 数组的算术和逻辑运算
- 傅里叶变换和用于图形操作的例程
  (傅里叶应用的例子可用声音叠加理解: 声音可以理解为各类波形, 正余弦波等, 复杂的声音其实是多种声音波形叠加而成, 通过傅里叶变换可以将不需要的不同频率的声音进行滤波操作, 从而达到去噪目的)
- 与线性代数有关的操作. Numpy 拥有线性代数和随机数生成的内置函数

## Numpy - Matlab 的替代之一
Numpy 与 Scipy 和 Matplotib(绘图库) 一起使用.


## Numpy - 环境
推荐使用 Anaconda, 自带整套 Python 科学计算的技术栈和库


## Numpy - Ndarray 对象
- ndarray 是 N 维数组类型, 是 Numpy 中最重要的对象
- ndarray 用来表示相同类型的元素集合, 操作速度比 Python 原生 array 更快, 操作类型更多
- ndarray 每个元素在内存中使用相同大小的块,
- ndarray 中每个元素是数据类型对象的对象(称为 dtype )?
- ndarray 类实例构造方法:numpy.array(object, dtype=None, copy=True, order=None, subok=False, ndmin=0)
```python
import numpy as np

a = np.array([1,2,3,4], ndmin=1)
print(a)

# 自动将数字转换为字符串
b = np.array([[1,2,3], ['a', 'b', 'c']])
print(b)

# python 原生的 array 可以支持各种类型元素
c = [1,2,3, 'c', 'b', 'a']
print(c)

# 指定数据类型和检测之前的数据类型
d = np.array([1,2,34,4], dtype=complex)
print(d)
print(a.dtype)
print(b.dtype)
# print(c.dtype)
print(d.dtype)
```

测试 numpy.array 接口的各类参数
```python
import numpy as np
# test object ==> interface
a = np.array(range(10))
print(a)

# 测试dtype
b = np.array(range(10), dtype = complex)
print(b)

# 测试 array 对象间赋值
#c = b # 该赋值会导致 c 和 b 实际共用一个存储
c = np.array(b, copy=True) # 会copy多一份出来进行赋值,不指向同一存储
print(c[1])
c[1] = 100
print(c)
print(b)
```

## Numpy - 数据类型
- bool 系: bool_, bool, bool8
- int 系: int_, intc, intp, int8, int16, int32, int64, uint8, uint16, uint32, uint64
- float 系: float_, float16, float32, float64
- complex 系: complex_, complex64, complex128

## 




