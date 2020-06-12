# -*- coding: utf-8 -*-
# _5.py
# 2020/6/11 22:14
# __author__ = 'zs'

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0., 5., 0.2)
# plot()方法返回list
line, line1 = plt.plot(t, t, 'r--', t, t**2, 'r--')
# print(isinstance(plt.plot(t, t, 'r--', t, t**2, 'r--'), list))
# 设置成False,关闭抗锯齿
line.set_antialiased(False)
plt.show()


