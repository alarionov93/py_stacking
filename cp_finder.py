import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img1 = cv.imread('/Volumes/Data/PhotoDevNew/Export2021/Export_13_07_21/0732-0733/IMG-0732.jpg')
img2 = cv.imread('/Volumes/Data/PhotoDevNew/Export2021/Export_13_07_21/0732-0733/IMG-0733.jpg')

orb = cv.ORB_create()

kp1 = orb.detect(img1, None)
kp1, des1 = orb.compute(img1, kp1)

kp2 = orb.detect(img2, None)
kp2, des2 = orb.compute(img2, kp2)
# res_view1 = cv.drawKeypoints(img1, kp1, None, color=(0,255,0), flags=0)
# plt.imshow(res_view1), plt.show()
# res_view2 = cv.drawKeypoints(img2, kp2, None, color=(0,255,0), flags=0)
# plt.imshow(res_view2), plt.show()

kp1[0].pt
kp1[0].pt
kp2[1].pt
kp2[1].pt

bf = cv.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# matches = sorted(matches, key = lambda x,y:y.distance)

# lambda x,y: x.distance <  0.7*y.distance
# cutted_matches = matches [ : len(matches)-1]
good = []
for m,n in matches:
	if m.distance <  0.7*n.distance:
		# print(np.array(kp0[m.trainIdx].pt) - np.array(kp1[m.queryIdx].pt))
		good.append(m)

src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)

M, mask = cv.findHomography(src_pts, dst_pts, cv.RANSAC, 5.0)

matchesMask = mask.ravel().tolist()

# h,w,d = img1.shape
# pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
dst = cv.getPerspectiveTransform(img2,M)

# img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:10],None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
# plt.imshow(img3),plt.show()


