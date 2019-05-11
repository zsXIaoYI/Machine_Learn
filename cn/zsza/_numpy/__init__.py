# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/20 下午5:33

import numpy as np
import matplotlib.pyplot as plt


m, n = (5, 3)
x = np.linspace(0, 1, m)
y = np.linspace(0, 1, n)

print(isinstance(x, np.ndarray))

print('x:\n', x)
print('y:\n', y)

X, Y = np.meshgrid(x, y)
print('X:\n', X)
print('Y:\n', Y)

plt.plot(X, Y, marker='.', color='blue', linestyle='none')
plt.show()
