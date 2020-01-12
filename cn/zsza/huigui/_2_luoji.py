# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/24 下午4:11

# 逻辑回归
from sklearn.linear_model import LogisticRegression
import numpy as np

x_train = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y_train = np.array([0, 1, 1, 0])


model = LogisticRegression()
model.fit(x_train, y_train)
print(model)

# 新样本
x_test = np.array([4, 5])
x_test.resize((1, 2))
y_pred = model.predict(x_test)

print('新样本的预测结果:', y_pred)
