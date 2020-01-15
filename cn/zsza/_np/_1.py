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
print(isinstance(s1, np.ndarray))

# 符合标准正态分布
sample2 = np.random.normal(size=(3, 2))
print(sample2)

# 生成一个从0到10的三行两列的矩阵
sample3 = np.random.randint(0, 10, size=(3, 2))
print(sample3)

# 将矩阵转换成x行3列，如果矩阵一共有6个元素，x就是2
print(sample3.reshape(-1, 3))

# 随机生成一个三行三列的矩阵
b1 = np.random.randn(3, 3)
print('b1:\n', b1)

print(b1[:, :2])  # 返回b1所有行的前两列元素

x = np.array([-1, 2, 3])
y = x > 0
# y返回[False  True  True]
print('y:', isinstance(y, np.ndarray))
# 返回[2 3]
print(x[y])

# z返回[0 1 1]
z = np.array(x > 0, dtype=np.int)
print('z:', z)

# float64标准双精度浮点数
arr = np.array([1, 2, 3], dtype=np.float64)
print('arr:', arr)
print('arr\'s type:', arr.dtype)

arr_int = arr.astype(np.int32)
print('arr_int:\n', arr_int)

print('Numpy数组进行切片\n')

arr1 = np.arange(15)
print('arr1:', arr1)

# 切片的赋值操作会影原有的数组，原有的数组会发生改变
arr1[8:12] = 30
print('切片之后的arr1:', arr1)

arr2 = np.arange(25).reshape((5, 5))
print('arr2:\n', arr2)

x_bool = np.array([0, 1, 2, 3, 1])
# 返回布尔型数组: [False  True False False  True]
print(x_bool == 1)

# 返回arr2的第二行和第五行
print(arr2[x_bool == 1])

# 布尔型索引还可以进行或操作
arr3 = arr2[(x_bool == 1) | (x_bool == 0)]
print('arr3:\n', arr3)


# 布尔型索引可以与切片结合使用
arr4 = arr2[x_bool == 1, 3:]
print('arr4:\n', arr4)

arr5 = np.arange(1, 13).reshape((4, 3))
print('arr5:\n', arr5)

# 返回arr5中大于7的元素的坐标，第一个数组是行坐标，第二个是列数组
print('np.where(arr5 > 7):\n', np.where(arr5 > 7))

# 打乱数组中的元素
np.random.shuffle(arr5)
print('after shuffle arr5: \n', arr5)

arr_min = np.array([[1, 3, 4],
                    [3, 1, 2],
                    [2, 5, 6]])
# axis=0: 列上的最小值,并返回行数组
print(np.argmin(arr_min, axis=0))

# axis=1: 行上的最小值,并返回列数组
print(np.argmin(arr_min, axis=1))

print('**************分隔符**************')
J = np.array([0, 1, 0])
# np.where返回tuple类型
print('np.where类型:\n', isinstance(np.where(J == 0), tuple))
print(np.where(J == 0)[0])


arr6 = np.arange(1, 17).reshape((4, 4))
print('arr6:\n', arr6)
# 返回arr6数组1、2行中第2和第3列的元素
print(arr6[np.ix_([1, 2], [2, 3])])
