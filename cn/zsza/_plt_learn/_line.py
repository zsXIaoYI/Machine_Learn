# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/8 下午10:33


from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='/Library/Fonts/Songti.ttc')
X = [[1], [4]]
y = [3, 5]

lr = LinearRegression().fit(X, y)
print(lr)

z = np.linspace(0, 5, 20)
plt.scatter(X, y, s=80)
plt.plot(z, lr.predict(z.reshape(-1, 1)), c='k')

plt.title('线性模型展示', FontProperties=font)
plt.show()

print(lr.predict(z.reshape(-1, 1)))
