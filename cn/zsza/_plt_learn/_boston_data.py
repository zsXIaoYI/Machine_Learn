# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/17 下午8:28


from sklearn.datasets import load_boston
import numpy as np
import matplotlib.pyplot as plt

boston = load_boston()
# print('boston:\n', boston)
boston.feature_names

data = boston.data
rms = data[:, 5]

prices = boston.target
print('rms:\n', rms)
print('prices:\n', prices)

plt.figure(figsize=(4, 3), facecolor='red')

plt.title('rms vs prices')
plt.xlabel('rm')
plt.ylabel('prices')

plt.scatter(rms, prices)
plt.show()
