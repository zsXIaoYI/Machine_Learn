# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/15 下午9:21

from numpy import genfromtxt

data = genfromtxt(r'data.csv', delimiter=',')
print(data)

x_data = data[:, :-1]  # 不包含最后一列
y_data = data[:, -1]
print('x_data:\n', x_data)
print('y_data:\n', y_data)
