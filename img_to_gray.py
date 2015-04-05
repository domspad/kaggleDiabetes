# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:41:17 2015

@author: pyoung
"""

import skimage.io as io
from skimage.color import rgb2gray
import glob

image_list = glob.glob('data/test_sample/*.jpeg')

for image in image_list:
    img_name = image.split('/')[-1]
    io.imsave('data/gray/' + img_name , rgb2gray(io.imread(image)))
