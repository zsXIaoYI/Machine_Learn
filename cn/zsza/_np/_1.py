# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/10 下午1:57

import numpy as np

# 随机生成一个0到1的三行两列的矩阵
sample1 = np.random.random((3, 2))
print(sample1)

# 随机生成一个0到4的数组,长度为8
s1 = np.random.randint(0, 5, 8)
print('s1:', s1)

# 符合标准正态分布
sample2 = np.random.normal(size=(3, 2))
print(sample2)

# 生成一个从0到10的三行两列的矩阵
sample3 = np.random.randint(0, 10, size=(3, 2))
print(sample3)

# 将矩阵转换成x行3列，如果矩阵一共有6个元素，x就是2
print(sample3.reshape(-1, 3))

x = np.array([-1, 2, 3])
y = x > 0
# y返回[False  True  True]
print('y:', isinstance(y, np.ndarray))
# 返回[2 3]
print(x[y])

