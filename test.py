import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

ret, img0 = cap.read()
orb = cv.ORB_create()
bfm = cv.BFMatcher()

kp0, des0 = orb.detectAndCompute(img0,None)
img_n = 0
l_a, l_b = 0, 0
while ret:
    ret, img1 = cap.read()
    kp1, des1 = orb.detectAndCompute(img1,None)
    
    matches = bfm.knnMatch(des0,des1,k=2)
    
    dxy = np.zeros((2))
    i = 0
    good = []
    for m,n in matches:
        
        if m.distance < 0.999*n.distance:
            try:
                delta = np.array(kp0[m.trainIdx].pt) - np.array(kp1[m.queryIdx].pt)
                if (abs(delta) < 10).all():
                    dxy += delta
                    i += 1
                    good += [m]
            except IndexError:
                pass
                # print(m.trainIdx, m.queryIdx)
    
    test_img = None
    test_img = cv.drawMatches(img0,kp0,img1,kp1,good,test_img)
    plt.imsave('%s.png' % img_n, test_img)
    print(img_n, dxy/i)

    img_n += 1
    
    img0, kp0, des0 = img1.copy(), kp1.copy(), des0.copy()
    
