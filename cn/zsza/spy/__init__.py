# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/18 下午9:40

import numpy as np
from scipy import sparse

matrix = np.eye(6)

sparse_matrix = sparse.csr_matrix(matrix)

print('对角矩阵:\n', matrix)

print('sparse存储的矩阵:\n', sparse_matrix)

