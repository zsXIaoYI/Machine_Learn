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

z = np.linspace(0, 5, 4)  # z是一个array
# -1:代表行数不确定, 2:代表返回两列
z = z.reshape((-1, 2))
print(z)
