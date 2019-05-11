# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/20 下午3:22

# 导入数据生成器
from sklearn.datasets import make_blobs
# 导入KNN分类器
from sklearn.neighbors import KNeighborsClassifier
# 导入数据拆分工具
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

data = make_blobs(n_samples=200, centers=2, random_state=8)
X, y = data

plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.spring, edgecolors='k')
plt.show()


