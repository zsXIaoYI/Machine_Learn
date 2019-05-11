# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/9 上午11:23

import numpy as np
from sklearn.naive_bayes import BernoulliNB


# 数据样X本特征构建, 样本特征分别是刮北风、闷热、多云、天气预报有雨
# 0: 否，1: 是

X = np.array([[0, 1, 0, 1],
             [1, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 1],
             [0, 1, 1, 0],
             [0, 1, 0, 1],
             [1, 0, 0, 1]])

# print(X[True])

y = np.array([0, 1, 1, 0, 1, 0, 0])
print(np.unique(y))  # 返回[0, 1]
counts = {}
for label in np.unique(y):
    # print(y == label)   返回true或false的一个array
    # [ True False False  True False  True  True]
    # X[y == label] 则返回下标为True的
    print(X[y == label])
    counts[label] = X[y == label].sum(axis=0)    # axis=0取列的和

print('features counts:\n{}'.format(counts))

print('---------贝叶斯拟合数据----------')

clf = BernoulliNB()
clf.fit(X, y)

# 要预测的这一天，没有挂北风，也不闷热，但是多云，天气预报说没有雨
Next_day = [[0, 0, 1, 0]]
pre = clf.predict(Next_day)

print('\n\n\n')
print('代码运行结果：')
print('========================\n')
print('pre:', pre)
if pre == [1]:
    print('下雨了，收衣服啦')
else:
    print('又是一个艳阳天')

