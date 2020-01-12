# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/24 下午3:44

# 线性回归
import numpy as np
from sklearn.linear_model import LinearRegression

# 4个样本，每个样本有4个特征
x_train = np.array([[1, 1, 2, 3], [1, 2, 1, 1], [2, 2, 2, 1], [2, 3, 2, 1]])
y_train = np.array([6, 8, 9, 11])


model = LinearRegression()
model.fit(x_train, y_train)

print(model)

# w
print(model.coef_)
# 偏执b
print(model.intercept_)
