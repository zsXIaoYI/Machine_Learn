# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/8 下午9:35


# 一次函数图像

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = 0.5*x + 3

plt.plot(x, y, c='orange')
plt.title('test')

plt.show()

z = np.linspace(0, 5, 3)  # z是一个array
z = z.reshape(-1, 1)
print(z)
