# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/21 下午5:04

import pandas as pd

x1 = pd.ExcelFile('1.2.test.xlsx')
print('sheet_name: {0}'.format(x1.sheet_names))

# 打印details这个sheet
df = x1.parse('details')
print(df)

# 把age这一列全部赋值为100
df['age'] = 100
# for index, row in df.iterrows():
#     row['age']  = 100
print(df)

print('*****************\n')

df2 = x1.parse('basic_info')

print(df2.isna())
avg = df2.mean(0)
print('平均成绩:\n', avg['score'])

df2 = df2.fillna(avg['score'])

print('df2:\n', df2)

# 生成新的excel
pd.DataFrame(df2).to_excel('new_excel.xlsx', sheet_name='new_basic_info')
