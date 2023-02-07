import sys
import cv2 as cv
import numpy as np
# from matplotlib import pyplot as plt
from itertools import product
from glob import glob

MIN_MATCH_COUNT = 100

try:
    path = sys.argv[1]
except IndexError:
    print('Usage: python3 imgs_cp.py /path/to/imgs/folder')
res_cp = []
res_img = np.zeros((1500,1500,3))

sift = cv.SIFT_create()
bf = cv.BFMatcher()

imgs = [cv.imread(x) for x in glob(f'{path}/*.jpg')]
for i1, i2 in product(imgs[1:], imgs[:-1]):
    
    kp1, des1 = sift.detectAndCompute(i1, None)
    kp2, des2 = sift.detectAndCompute(i2, None)
    res_cp += [((kp1,des1),(kp2,des2))]
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m,n in matches:
        if m.distance <  0.85*n.distance:
            good.append(m)
    if len(good) > MIN_MATCH_COUNT:
        src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ])
        src_median = np.median(src_pts[:, :1])
        dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ])
        dst_median = np.median(dst_pts[:, :1])
        print(src_median, dst_median)
        h, stat = cv.findHomography(src_pts, dst_pts)
        img_out = cv.warpPerspective(imgs[i+1], h, (imgs[i].shape[1]+300, imgs[i].shape[0]+200))
        #img_out[:imgs[i+1].shape[0],:imgs[i+1].shape[1]] = imgs[i+1]v
        cv.imwrite('res_img.jpg', img_out)

