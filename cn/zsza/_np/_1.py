# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/10 下午1:57

import numpy as np

# 随机生成一个0到1的三行两列的矩阵
sample1 = np.random.random((3, 2))
print(sample1)

# 随机生成一个0到4的数组,长度为8
s1 = np.random.randint(0, 5, 8)
print('s1:', s1)
print(isinstance(s1, np.ndarray))

# 符合标准正态分布
sample2 = np.random.normal(size=(3, 2))
print(sample2)

# 生成一个从0到10的三行两列的矩阵
sample3 = np.random.randint(0, 10, size=(3, 2))
print(sample3)

# 将矩阵转换成x行3列，如果矩阵一共有6个元素，x就是2
print(sample3.reshape(-1, 3))


# 随机生成一个三行三列的矩阵
b1 = np.random.randn(3, 3)
print('b1:\n', b1)

print(b1[:, :2])    # 返回b1所有行的前两列元素

x = np.array([-1, 2, 3])
y = x > 0
# y返回[False  True  True]
print('y:', isinstance(y, np.ndarray))
# 返回[2 3]
print(x[y])

# z返回[0 1 1]
z = np.array(x > 0, dtype=np.int)
print('z:', z)

# float64标准双精度浮点数
arr = np.array([1, 2, 3], dtype=np.float64)
print('arr:', arr)
print('arr\'s type:', arr.dtype)

arr_int = arr.astype(np.int32)
print('arr_int:\n', arr_int)


print('Numpy数组进行切片\n')

arr1 = np.arange(15)
print('arr1:', arr1)

# 切片的赋值操作会影原有的数组，原有的数组会发生改变
arr1[8:12] = 30
print('切片之后的arr1:', arr1)

arr2 = np.arange(25).reshape((5, 5))
print('arr2:\n', arr2)

x_bool = np.array([0, 1, 2, 3, 1])
print(x_bool == 1)

# 返回arr2的第二行和第五行
print(arr2[x_bool == 1])
