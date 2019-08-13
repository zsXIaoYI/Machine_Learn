# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2019/8/13 22:54
# @File: __init__.py.py
# __author__ = 'zs'


import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

df = pd.read_csv('1.5.2.data.csv')
X = df.values

# fig = plt.figure()
# ax = Axes3D(fig)

# ax.scatter(X[:, 0], X[:, 1], X[:, 1])

pca = PCA(n_components=2)
Xlow = pca.fit_transform(X)

plt.scatter(Xlow[:, 0], Xlow[:, 1])
plt.show()

