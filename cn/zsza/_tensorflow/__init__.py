# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/2 下午10:58


import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

hello = tf.constant('孙')

with tf.Session() as sess:
    output = sess.run(hello)
    print(output.decode('utf-8'))


a = tf.constant([1., 2.], name='a')
b = tf.constant([2., 3.], name='b')

print('a:\n', a)
result = a + b
print(a.graph is tf.get_default_graph())

with tf.Session() as sess:
    out = sess.run(result)
    print(out)
