# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/9/6 上午10:55

from mxnet import nd

# 生成一个10维的特征向量
a = nd.ones(shape=10)
print(a)


features = nd.random.normal(scale=1, shape=(1, 2))

