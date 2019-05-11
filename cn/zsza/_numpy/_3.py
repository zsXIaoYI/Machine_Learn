# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/11 下午3:54

import numpy as np

arr = np.arange(2, 14)

print(arr)
print(arr[2:-1])   # 从第二个到倒数第二个
print(arr[-2:])

a1 = arr.reshape((4, 3))
print(a1)

for i in a1.T:  # 迭代转置矩阵，其实就是迭代原矩阵的列
    print(i)

# 迭代所有的元素
for j in arr.flat:
    print(j)
