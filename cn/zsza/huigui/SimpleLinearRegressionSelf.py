# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2020/1/18 10:21
# @File: SimpleLinearRegressionSelf.py
# __author__ = 'zs'


import numpy as np


class SimpleRegressionSelf(object):
    def __init__(self):
        '''初始化一个特征的线性回归模型'''
        self.a_ = None
        self.b_ = None

    # 训练方法
    def fit(self, x_train, y_train):
        assert x_train.ndim == 1
        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)
        denominator = 0.0
        numerator = 0.0
        for x_i, y_i in zip(x_train, y_train):
            numerator += (x_i - x_mean) * (y_i - y_mean)
            denominator += (x_i - x_mean) ** 2
        self.a_ = numerator / denominator
        self.b_ = y_mean - self.a_ * x_mean
        return self

    # 预测函数
    def predict(self, x_test_group):
        return np.array([self._predict(x_test) for x_test in x_test_group])

    def _predict(self, x_test):
        return self.a_ * x_test + self.b_

    def mean_squared_error(self, y_true, y_predict):
        return np.sum((y_true - y_predict) ** 2) / len(y_true)

    def r_square(self, y_true, y_predict):
        return 1 - (self.mean_squared_error(y_true, y_predict) / np.var(y_true))


if __name__ == '__main__':
    x = np.array([1, 2, 4, 6, 8])
    y = np.array([2, 5, 7, 8, 9])
    lr = SimpleRegressionSelf()
    lr.fit(x, y)
    print(lr.predict([7]))
    print(lr.r_square([8, 9], lr.predict([6, 8])))
