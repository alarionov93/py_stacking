import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


res_cp = []
res_img = np.zeros((1500,1500,3))
for i in range(len(imgs)-1):
    kp, des = sift.detectAndCompute(imgs[i+1], None)
    kp1, des1 = sift.detectAndCompute(imgs[i], None)
    res_cp += [((kp,des),(kp1,des1))]
    matches = bf.knnMatch(des, des1, k=2)
    good = []
    for m,n in matches:
        if m.distance <  0.85*n.distance:
            good.append(m)
    src_pts = np.float32([ kp[m.queryIdx].pt for m in good ])
    src_median = np.median(src_pts[:, :1])
    dst_median = np.median(dst_pts[:, :1])
    print(src_median, dst_median)
    dst_pts = np.float32([ kp1[m.trainIdx].pt for m in good ])
    h, stat = cv.findHomography(src_pts, dst_pts)
    img_out = cv.warpPerspective(imgs[i+1], h, (imgs[i].shape[1]+300, imgs[i].shape[0]+200))
    #img_out[:imgs[i+1].shape[0],:imgs[i+1].shape[1]] = imgs[i+1]
    cv.imwrite('res_img.jpg', img_out)



