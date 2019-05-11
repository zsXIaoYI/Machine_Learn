# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2019/5/11 21:05
# @File: _2.py
# __author__ = 'zs'

# 矩阵的合并
import numpy as np
ar1 = np.array([[1, 2],
                [3, 4]])

ar2 = np.array([[11, 12],
                [13, 14]])

print(np.vstack((ar1, ar2)))  # 垂直合并
print(np.hstack((ar1, ar2)))  # 水平合并

print(np.concatenate((ar1, ar2), axis=0))  # 0:垂直, 1:水平


ar = np.array([1, 2, 3])
print(ar)
print(ar.shape)  # 返回(3, )

ar1_2 = ar[np.newaxis, :]  # 变成一行三列的矩阵
print(ar1_2)
print(ar.reshape((-1, 1)))
