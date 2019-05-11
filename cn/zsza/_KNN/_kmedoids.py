# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/29 下午2:37


from sklearn.metrics.pairwise import pairwise_distances
import numpy as np

# 导入GitHub上的源代码
import kmedoids

# 3 points in dataset
data = np.array([[1,1],
                [2,2],
                [10,10]])

# distance matrix
D = pairwise_distances(data, metric='euclidean')

# split into 2 clusters
M, C = kmedoids.kMedoids(D, 2)

print('medoids:')
for point_idx in M:
    print( data[point_idx] )

print('')
print('clustering result:')
for label in C:
    for point_idx in C[label]:
        print('label {0}:　{1}'.format(label, data[point_idx]))
