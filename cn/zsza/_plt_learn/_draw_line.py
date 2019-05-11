# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/15 下午10:05

from sklearn.linear_model import LinearRegression
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import numpy as np

font = FontProperties(fname='/Library/Fonts/Songti.ttc')

# y = 2x +3
# (1, 5)和 (3, 9)两个坐标点
X = [[1], [3]]
y = [5, 9]

lr = LinearRegression().fit(X, y)
# z从0到5范围内取两个数据(这两个数据符合等差数列)
z = np.linspace(0, 5, 2)

print('z:\n', z)
z1 = z.reshape((-1, 1))
print('z1:\n', z1)

# 把X, y坐标点画到坐标轴上
plt.scatter(X, y, s=80)
# 拟合上去 z=[0. 5.]
# lr.predict(z.reshape(-1, 1)) = [3. 13.]

plt.plot(z, lr.predict(z.reshape(-1, 1)), c='r')
plt.title('Straight Line', FontProperties=font)

print('斜率:', lr.coef_[0])
print('截距:', lr.intercept_)
plt.show()


