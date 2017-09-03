# Python Learning Note
## 注意生成器的使用
生成器用过一次循环后即不可再用, 这点需要注意, 下面的代码出现的问题就是这个导致的.
下面这段代码本意是生成两个数组, 拟合数据关系: y=x^2, 为了省内存, 我使用了生成器, 但代码运行后发现 y 是空的, 经过思考, 确认是 x 在转为 X 时已经被使用过导致后面不支持再次循环.
```python
import numpy as np
x = (i for i in range(10))
y = ( i*i for i in x)

X = np.array(list(x)).transpose()
print(X)
Y = list(y)
for i in Y:
    print(i)

```