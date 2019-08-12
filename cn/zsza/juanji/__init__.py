# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/5/8 下午5:59

# 依赖pillow
from scipy.misc import imread
import pandas as pd
import imageio
from PIL import Image
import numpy as np

img = imageio.imread('2.png')
# img = imread('2.png')
print(img.shape)
img_df = pd.DataFrame(img.reshape((-1, 2)))
img_df.to_csv('2.csv')


img1 = np.array(Image.open('zx.jpg'))
print(img1.shape)  # 返回(10, 10, 3)
print(img1)
