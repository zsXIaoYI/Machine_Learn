# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/1/6 20:30
# @File: _1.py
# __author__ = 'zs'

import pandas as pd
import numpy as np

s1 = pd.Series([1, 2, 3, 4, 5, np.nan])
print('s1:\n', s1)

s2 = pd.Series([1, 2, 3], index=['one', 'two', 'three'])
print('s2:\n', s2)


s3 = pd.date_range('20130201', periods=3)
print('s3:\n', s3)


s4 = pd.DataFrame(np.random.randn(3, 3), index=s3, columns=list('ABC'))
print('s4:\n', s4)

s5 = pd.Series(1, index=list(range(4)), dtype='float32')
print('s5:\n', s5)

# 返回结果的索引按照字典顺序排列
s6 = pd.Series({'one': 1, 'two': 2, 'three': 3, 'four': np.nan})
print('s2 + s6: \n', s2 + s6)
