# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/9/27 下午2:30

# 跃阶函数

import numpy as np
import matplotlib.pyplot as plt


def step_function(_x):
    return np.array(_x > 0, dtype=np.int)


x = np.arange(-5.0, 5, 0.1)
y = step_function(x)

plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
