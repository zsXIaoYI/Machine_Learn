# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/23 下午10:04

from sklearn.linear_model import LinearRegression
import numpy as np

# y = w1*x1 + w2*x2 + b
x_train = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y_train = np.array([6, 8, 9, 11])

model = LinearRegression()

model.fit(x_train, y_train)

print(model.coef_)  # 系数
print(model.intercept_)   # 截距
