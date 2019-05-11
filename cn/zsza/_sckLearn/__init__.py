# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/13 下午9:21


from sklearn.datasets import make_blobs
from sklearn.datasets import make_regression

X, y = make_blobs(n_samples=5, centers=2, random_state=8)
print(X, y)

print('>>>>>>>>>>>><<<<<<<<<<<<<')

X1, y1 = make_regression(n_samples=5, n_features=2, n_informative=1, random_state=1)

print(X1)
print('.......')
print(y1)
