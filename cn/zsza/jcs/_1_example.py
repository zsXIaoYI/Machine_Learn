# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/16 下午9:06


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import tree,datasets
from sklearn.model_selection import train_test_split

wine = datasets.load_wine()  # 返回一个dict
# print('酒的数据:\n', wine)

X = wine.data[:, :2]
y = wine.target
# print(X)
# print(y)

X_train, X_test, y_train, y_test = train_test_split(X, y)
print('X_train:\n', X_train)
print('X_test:\n', X_test)

clf = tree.DecisionTreeClassifier(max_depth=1)
clf.fit(X_train, y_train)
print('clf:\n', clf)