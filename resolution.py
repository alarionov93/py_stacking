from itertools import product
from glob import glob
from random import choice
from PIL import Image

import sys
import numpy as np
import cv2 as cv

dir_name = sys.argv[1]

#newname = f'res_{imgs[0].split("/")[-1].split(".")[0]}_{imgs[-1].split("/")[-1].split(".")[0]}'

imgs_a = [cv.imread(x, 1) for x in glob(f'{dir_name}/*.png')]

w,h = imgs_a[0].shape[1],imgs_a[0].shape[0]

iimages = np.zeros((w*4,h*4,3), dtype=np.uint8)

a = [0,1,2,3]
b = [0,1,2,3]
in_arr_a = []
in_arr_b = []
for x in range(len(a)):
    el = choice(a)
    in_arr_a.append(el)
    a.remove(el)

for x in range(len(b)):
    el = choice(b)
    in_arr_b.append(el)
    b.remove(el)
# TODO: replace for loops by place (to make random coordinates every iteration on source pixel)
n = 0
for dy, dx in product(in_arr_a, in_arr_b):
    print(dx,dy)
    for y,x in product(range(w), range(h)):
        iimages[y*4+dy,x*4+dx] = imgs_a[n][x, y]
    n+=1

# iii = np.sum(iimages, 0)
# TODO: newname!
cv.imwrite(f'{dir_name}/16x_test_res.png', iimages)

