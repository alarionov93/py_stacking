from itertools import product
from glob import glob
from random import shuffle
from PIL import Image

import sys
import numpy as np
import cv2 as cv

dir_name = sys.argv[1]

imgs = glob(f'{dir_name}/*.png')
newname = f'res_{imgs[0].split("/")[-1].split(".")[0]}_{imgs[-1].split("/")[-1].split(".")[0]}'
imgs_a = [cv.imread(x, 1) for x in imgs]

w,h = imgs_a[0].shape[1],imgs_a[0].shape[0]

iimages = np.zeros((w*4,h*4,3), dtype=np.uint8)
a = b = [0,1,2,3]
n = 0
f = open('err.log', 'w')
for dx, dy in product(a, b):
    # print(dx,dy)
    # dx = dy = 0
    # shuffle(imgs_a)
    for y,x in product(range(w), range(h)):
        iimages[y*4+dy,x*4+dx] = imgs_a[n][x, y]
        f.write(f'{y*4+dy}, {x*4+dx}, {n}, {x}, {y}\n')
    n+=1
f.close()
# iii = np.sum(iimages, 0)
# TODO: newname!
cv.imwrite(f'{dir_name}/{newname}.jpg', iimages)

