# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/10 下午5:52

import numpy as np

# 矩阵的乘法

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])

print(A * B)
print(A.dot(B))   # 矩阵乘法

# print(np.random)
a = np.random.random((2, 3))  # 随机生成一个2行3列的矩阵
print(a)

b = np.arange(12).reshape((3, 4))
print(b)
print(b.max())

print(b.sum(axis=0))   # 计算矩阵的每一列的和
print(b.sum(axis=1))   # 计算矩阵的每一行的和

print(np.argmin(b))  # 求最小值的索引


c = np.array([2., 3., 4., 6.])
print('c:', c)
print(c.dtype)

d = np.array([[9, 5, 6, 3, 6, 8, 0, 7, 9, 7, 2, 7],
              [1, 4, 9, 2, 2, 1, 0, 6, 2, 2, 4, 0]])
print(np.split(d, 3, axis=1))         # axis=1 垂直分割


x_test = np.array([4, 5])
print(x_test)

x_test.resize((1, 2))
print(x_test)

# 从1开始，每隔2个取一个值
r1 = np.arange(1, 10, 2)
print('r1:\n', r1)
