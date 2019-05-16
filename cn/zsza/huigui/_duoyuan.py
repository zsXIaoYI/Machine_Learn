# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/15 下午9:21

import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = genfromtxt(r'data.csv', delimiter=',')
print(data)

x_data = data[:, :-1]  # 不包含最后一列
y_data = data[:, -1]
print('x_data:\n', x_data)
print('y_data:\n', y_data)

print(float(len(x_data)))

# 学习率
lr = 0.0001
# 参数
theta0 = 0
theta1 = 0
theta2 = 0

# 最大迭代次数
epochs = 1000


def compute_error(theta0, theta1, theta2, x_data, y_data):
    totalError = 0
    for i in range(0, len(x_data)):
        totalError += (y_data[i] - (theta1 * x_data[i, 0] + theta2 * x_data[i, 1] + theta0)) ** 2
    return totalError / float(len(x_data))


def gradient_descent_runner(x_data, y_data, theta0, theta1, theta2, lr, epochs):
    # 计算总数据量
    m = float(len(x_data))

    for i in range(epochs):
        theta0_grand = 0
        theta1_grand = 0
        theta2_grand = 0

        for j in range(0, len(x_data)):
            theta0_grand += (1 / m) * ((theta1 * x_data[j, 0] + theta2 * x_data[j, 1] + theta0) - y_data[j])
            theta1_grand += (1 / m) * x_data[j, 0] * ((theta1 * x_data[j, 0] + theta2 * x_data[j, 1] + theta0) - y_data[j])
            theta2_grand += (1 / m) * x_data[j, 1] * ((theta1 * x_data[j, 0] + theta2 * x_data[j, 1] + theta0) - y_data[j])

        theta0 = theta0 - (lr * theta0_grand)
        theta1 = theta1 - (lr * theta1_grand)
        theta2 = theta2 - (lr * theta2_grand)

    return theta0, theta1, theta2


print('Starting theta0 = {0}, theta1 = {1}, theta2 = {2}, error = {3}'
      .format(theta0, theta1, theta2, compute_error(theta0, theta1, theta2, x_data, y_data)))

print('Running\n')

theta0, theta1, theta2 = gradient_descent_runner(x_data, y_data, theta0, theta1, theta2, lr, epochs)

print('After {0} iterations theta0 = {1}, theta1 = {2}, theta2 = {3}, error = {4}'
      .format(epochs, theta0, theta1, theta2, compute_error(theta0, theta1, theta2, x_data, y_data)))

ax = plt.figure().add_subplot(111, projection='3d')
ax.scatter(x_data[:, 0], x_data[:, 1], y_data, c='r', marker='o', s=100)
x0 = x_data[:, 0]
x1 = x_data[:, 1]

x0, x1 = np.meshgrid(x0, x1)
z = theta0 + x0 * theta1 + x1 * theta2
# 画3d图
ax.plot_surface(x0, x1, z)

ax.set_xlabel('Miles')
ax.set_ylabel('Number of Deliveries')
ax.set_zlabel('Time')

plt.show()
