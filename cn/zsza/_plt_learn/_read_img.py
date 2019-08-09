# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/7/4 下午1:52


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open('xx.png'))

print(img.shape)
print(img)
