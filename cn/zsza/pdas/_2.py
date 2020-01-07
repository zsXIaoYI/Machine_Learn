# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/1/7 19:49
# @File: _2.py
# __author__ = 'zs'


import pandas as pd
import numpy as np

# 声明一个dict
data = {'Name': ['小红', '小黑', '小白'],
        'City': ['北京', '东京', '夏威夷'],
        'Age': [20, 22, 26]}

df = pd.DataFrame(data)
print('df:\n', df)
print('\n')
print(df[df.City != '北京'])

print('前两行:\n', df.head(2))
print('df的维度:', df.shape)

print('df的Age列:\n', df['Age'])
print('df的第一行:\n', df.loc[1])
print('df中Age这一列的第0个和第2个:\n', df.loc[df.index[[0, 2]], 'Age'])

# data中没有Gender这个key,df2则显示NaN
df2 = pd.DataFrame(data, columns=['Name', 'City', 'Age', 'Gender'])
print('df2:\n', df2)

# 给df2中Gender这一列的第0个和第1个赋值
df2['Gender'] = pd.Series(['male', 'female'], index=[0, 1])
print('after df2:\n', df2)

print('*******迭代df*****\n')

df1 = pd.DataFrame(np.random.randn(4, 3), columns=['c1', 'c2', 'c3'])
print(df1)

for index, row in df1.iterrows():
    row['c2'] = 10

print(df1)
