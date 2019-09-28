# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/9/10 下午7:39

import numpy as np

# 用1填充矩阵的所有元素
a = np.ones_like([[1, 2],
                  [3, 4]])
print(a)

# np.arange(0, 60, 10).reshape((-1, 1))
# 上面返回从0开始，每隔10个数，不超过60的N行一列矩阵
# [[ 0  1  2  3  4  5]
#  [10 11 12 13 14 15]
#  [20 21 22 23 24 25]
#  [30 31 32 33 34 35]
#  [40 41 42 43 44 45]
#  [50 51 52 53 54 55]]
b = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)
print(b)

# 通过dtype指定元素类型
d = np.array([[1, 2],
              [3, 4]], dtype=np.float)
print(d)

f = np.arange(1, 10, 0.5)
print(f)

#  创建起始值为2^0，终止值为2^10(包括)，有5个数的等比数列,endpoint=False不包含终止值
g = np.logspace(0, 10, 5, endpoint=False, base=2)
print(g)

s = 'abcdz'
h = np.fromstring(s, dtype=np.int8)
print(h)
