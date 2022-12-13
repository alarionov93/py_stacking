import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1 = cv.imread('/Users/sanya/Work/py_stacking/tst_imgs/IMG-1874_s.jpg')
img2 = cv.imread('/Users/sanya/Work/py_stacking/tst_imgs/IMG-1873_s.jpg')

# orb = cv.ORB_create()
sift = cv.SIFT_create()

# kp1 = orb.detect(img1, None)
# [ TODO: !!!!! ] for by pairs of files: промискуитетная программа!!!!!!
#  Все со всеми должны спариться!!
kp1, des1 = sift.detectAndCompute(img1, None)

# kp2 = orb.detect(img2, None)
kp2, des2 = sift.detectAndCompute(img2, None)
# res_view1 = cv.drawKeypoints(img1, kp1, None, color=(0,255,0), flags=0)
# plt.imshow(res_view1), plt.show()
# res_view2 = cv.drawKeypoints(img2, kp2, None, color=(0,255,0), flags=0)
# plt.imshow(res_view2), plt.show()

# kp1[0].pt
# kp1[0].pt
# kp2[1].pt
# kp2[1].pt

bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# matches = sorted(matches, key = lambda x,y:y.distance)

# lambda x,y: x.distance <  0.7*y.distance
# cutted_matches = matches [ : len(matches)-1]
good = []
for m,n in matches:
	if m.distance <  0.85*n.distance: # 0.85 - ok; TODO: other - test it
		good.append(m)

		# print(np.array(kp0[m.trainIdx].pt) - np.array(kp1[m.queryIdx].pt))

src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ])
dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ])

h, stat = cv.findHomography(src_pts, dst_pts)
# cv.drawKeypoints(img1, kp1, img1)
# cv.drawKeypoints(img2, kp2, img2)
for y,x in src_pts:
	cv.circle(img1,(int(y),int(x)), 4, (0,0,255), -1)

for y,x in dst_pts:
	cv.circle(img2,(int(y),int(x)), 4, (0,255,0), -1)

img_out = cv.warpPerspective(img1, h, (img2.shape[1]+300, img2.shape[0]+200))
cv.imwrite('/Users/sanya/Work/py_stacking/tst_imgs/IMG-1874_warped.jpg', img_out)
cv.imwrite('/Users/sanya/Work/py_stacking/tst_imgs/IMG-1873_kp.jpg', img2)

# M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)

# matchesMask = mask.ravel().tolist()

# h,w,d = img1.shape
# pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
# dst = cv.getPerspectiveTransform(img2,M)

# img3 = cv.drawMatches(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# plt.imshow(img3),plt.show()

