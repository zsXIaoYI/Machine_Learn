# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/18 下午11:24

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20, 20, 10)
y = x ** 3 + 2 * x ** 2 + 6 * x + 5

plt.plot(x, y, marker='v')
plt.show()
