# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/18 下午11:01

import pandas as pd

data = {'Name': ['小红', '小黑', '小白'],
        'City': ['北京', '东京', '夏威夷'],
        'Age': [20, 22, 26]}

data_frame = pd.DataFrame(data)
print('data_frame:\n', data_frame)
print('\n')
print(data_frame[data_frame.City != '北京'])
