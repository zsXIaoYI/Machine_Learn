# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/14 下午12:19


# Numpy中的方法reshape与resize的区别
# reshape：有返回值，不对原始多维数组进行修改
# resize：无返回值，会对原始多维数组进行修改

import numpy as np

a = np.arange(15)
print('a:\n', a)  # [0, 1, ...... 14]

a1 = a.reshape((3, 5))
print('a1:\n', a1)
# reshape操作后，数组a并没有被修改
print('reshape操作后a:\n', a)

a2 = a.resize((5, 3))
print('a2:\n', a2)  # a2返回None
print('resize操作后的a:\n', a)  # a返回5行3列的数据

# 返回第三行,前两列的元素
print(a[2, 0:2])  # 返回[6, 7]


# 写一个函数，输入数组维数，能返回一个二维数组，二维数组中k行的值全为k
def fn(n):
    result = np.arange(n * n).reshape((n, n))
    result[(n - 1), 0:n] = n
    return result


print(fn(3))

b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print('b:\n', b)

print('*********矩阵的乘法********')

A = np.array([[1, 2, 4], [4, 5, 3]])
B = np.array([[1, 4], [3, 2], [2, 5]])

print('A:\n', A)
print('B:\n', B)

print(A.dot(B))

print('A的转置矩阵:\n', A.transpose())

print('************求期望、方差、标准差**************')

data = [10, 30, 40, 50, 10]
print('期望:', np.mean(data))
print('方差:', np.var(data))
print('标准差:', np.std(data))

x = [1, 2, 3, 7]
# y = [4, 5, 6]
y = np.array([4, 5, 6])

print('y:\n', y.reshape((-1, 3)))
print('\n')

x1, y1 = np.meshgrid(x, y)
print('x1:\n', x1)
print('y1:\n', y1)

print('-------------')

A = np.array([[1, 2], [3, 4]])
# B为2行1列的矩阵，2行1列的矩阵只有一个方括号
B = np.array([7, 8])

print('B的维度:', B.shape)
C = np.dot(A, B)
print('C：', C)
