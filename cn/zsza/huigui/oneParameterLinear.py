# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/1/18 10:10
# @File: oneParameterLinear.py
# __author__ = 'zs'

# 只有一个特征的线性回归
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    x = np.array([1, 2, 4, 6, 8])
    y = np.array([2, 5, 7, 8, 9])
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    denominator = 0.0
    numerator = 0.0
    for x_i, y_i in zip(x, y):
        numerator += (x_i - x_mean) * (y_i - y_mean)
        denominator += (x_i - x_mean) ** 2
    a = numerator / denominator
    b = y_mean - a * x_mean
    y_predict = a * x + b
    plt.scatter(x, y, color='r')
    plt.plot(x, y_predict, color='b')
    plt.xlabel('x轴')
    plt.ylabel('y轴')
    plt.show()

