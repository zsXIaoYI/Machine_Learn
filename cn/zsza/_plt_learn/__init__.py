# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/15 下午9:55

# y = kx + b图像学习
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 5, 2)
print('x:\n', x)
y = 0.5 * x + 3

plt.plot(x, y, c='red')
plt.title('Straight Line')
plt.show()


