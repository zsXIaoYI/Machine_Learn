# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/28 下午6:34

from sklearn.cluster import KMeans
import numpy as np


X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)
print(kmeans.predict([[0, 0], [4, 4]]))

print(kmeans.cluster_centers_)  # 类簇中心
