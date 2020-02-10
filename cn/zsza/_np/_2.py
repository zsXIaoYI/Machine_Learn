# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2019/5/11 21:05
# @File: _2.py
# __author__ = 'zs'

# 矩阵的合并

import numpy as np
ar1 = np.array([[1, 2],
                [3, 4]])

print('arr1的类型:', ar1.dtype)

print(ar1[:, 0])  # 返回第一列
print(ar1[:, 0, np.newaxis])  # 在上面基础上增加一个维度，返回两行一列的矩阵,
print(isinstance(ar1[:, 0, np.newaxis], np.ndarray))

print('****************分隔符****************')

ar2 = np.array([[11, 12],
                [13, 14]])

print(np.vstack((ar1, ar2)))  # 垂直合并
print(np.hstack((ar1, ar2)))  # 水平合并

print(np.concatenate((ar1, ar2), axis=0))  # 0:垂直, 1:水平


ar = np.array([1, 2, 3])  # 一维数组
print(ar)
print(ar.shape)  # 返回(3, )

ar1_2 = ar[np.newaxis, :]  # 变成一行三列的矩阵
print(ar1_2)
print(ar.reshape((-1, 1)))

arr2 = np.arange(9).reshape((3, 3))
print('arr2:\n', arr2)

# axis=0 每列求和
print('arr2每行求和:', arr2.sum(axis=1))

# 循环遍历arr2
for row in arr2:
    for ele in row:
        print(ele)

arr3 = np.array([3, 4])
arr4 = np.array([2, 6])
print('数组相减:\n', arr3 - arr4)
print('两数组相减后,各元素求平方,最后求和:\n', np.sum((arr3 - arr4) ** 2))

arr5 = np.array([[3, 6],
                 [2, 4]])
'''
np.var:
 axis=1：求行上的方差
 axis=0：求列上的方差
'''
print(np.var(arr5, axis=0))


# 求方差
print(np.var([6, 4, 2]))


