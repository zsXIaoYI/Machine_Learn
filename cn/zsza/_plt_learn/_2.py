# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/19 下午5:49

import matplotlib.pyplot as plt
import numpy as np


x = np.array([1, 2])
y = np.array([3, 5])

# c:颜色
# marker:点的形状
plt.scatter(x, y, c='r', marker='v')
plt.show()
