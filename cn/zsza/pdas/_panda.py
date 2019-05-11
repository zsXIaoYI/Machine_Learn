# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/3/10 上午11:51


import pandas as pd

x1 = pd.ExcelFile('/PyCharm_Space/untitled/file/test.xlsx')
print('sheet_names: {0}'.format(x1.sheet_names))

df = x1.parse('details')

print(df)
print(df.values)

avg = df.mean(0)
print('平均年龄:', avg['age'])

for index, row in df.iterrows():
    print(index)
    name = row['name']

    # row['age'] = 30
    # age = row['age']

    country = row['country']
    print('{0}, {1}'.format(country, name))

# pandas series

d1 = {'name': pd.Series(['Tom', 'Jack', 'Amy']), 'Age': pd.Series([12, 15, 24]),
      'weight': pd.Series([30, 50, 60])}
df1 = pd.DataFrame(d1)
print('our data series is:')
print(df1)

print(df1.shape)
print(df1.sum(0))  # by colum
print(df1.sum(1))  # by row
print(df1.sum())

print(df1.std())  # 除以n-1
print(df1.var())  # 开根号是上面的值
# print(df1.describe())

print(324 + 4 + 144 + 484 + 324)
print(1280 / 5)
