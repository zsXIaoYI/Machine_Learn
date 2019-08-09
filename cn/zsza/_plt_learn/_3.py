# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/16 上午11:37

from sklearn import datasets
import matplotlib.pyplot as plt

# noise 越大的话，点就会越来越离散，例如 noise 由 10 变为 50.
X, y = datasets.make_regression(n_samples=20, n_features=1, n_targets=1, noise=20, random_state=80)

print(X)
print(y)
plt.scatter(X, y, s=11)
plt.show()



