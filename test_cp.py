import cv2 as cv
import numpy as np
from glob import glob
from matplotlib import pyplot as plt

imgs = glob('/Users/sanya/Pictures/tmp/*.jpeg')
imgs0 = [cv.imread(img,1) for img in imgs]

first_img = imgs0[0]

orb = cv.ORB_create()
kps = []
dess = []
for idx in range(0,len(imgs0)):
    kp = orb.detect(imgs0[idx], None)
    kp, des = orb.compute(imgs0[idx], kp)
    kps.append(kp)
    dess.append(des)

bf = cv.BFMatcher()

for idx in range(1,len(imgs0)):
    matches = bf.knnMatch(dess[0], dess[idx], k=2)
    good = []
    for m,n in matches:
        if m.distance <  0.7*n.distance: # 0.85 - ok; TODO: other - test it
            good.append(m)
    src_pts = np.float32([ kps[0][m.queryIdx].pt for m in good ])
    dst_pts = np.float32([ kps[idx][m.trainIdx].pt for m in good ])
    #print(len(src_pts), len(dst_pts))
    h, stat = cv.findHomography(src_pts, dst_pts)
    # print(h)
    for y,x in src_pts:
        cv.circle(first_img,(int(y),int(x)), 4, (0,0,255), -1)
    for y,x in dst_pts:
        cv.circle(imgs0[idx],(int(y),int(x)), 4, (0,255,0), -1)
    img_out = cv.warpPerspective(imgs0[idx], h, (first_img.shape[1], first_img.shape[0]))
    cv.imwrite('/Users/sanya/Pictures/res_img_0.jpeg', imgs0[0])
    cv.imwrite('/Users/sanya/Pictures/res_img_%s.jpeg' % idx, imgs0[idx])


# old scan_rgb_img.py
# curve_cord_X = np.array([], dtype=int)
# curve_cord_Y = np.array([], dtype=int)

# for r, coords in res:
#     X,Y = np.where(r>250)
#     X_ = X+coords[0]*shift
#     Y_ = Y+coords[1]*shift
#     a,b,c = np.polyfit(X_,Y_,2)
#     #print(coords[0],coords[1])
#     plt.plot(X_, X_**2 * a + X_ * b + c)
#     # plt.plot(X_, Y_)
#     # plt.plot(X_[0], Y_[0], 'ro:')
#     #plt.plot(X_[-1],Y_[-1], 'ro:')
#     # lst = []
#     # print("X:")
#     # print(X_)
#     # print("Y:")
#     # print(Y_)
#     # curve_cord_X = np.append(curve_cord_X, X_.astype(int))
#     # curve_cord_Y = np.append(curve_cord_Y, (X_**2 * a + X_ * b + c).astype(int))
#     # del lst
#     avg_x = ((X_[0]+X_[-1])/2).astype(int)
#     avg_y = (((X_**2 * a + X_ * b + c)[0]+(X_**2 * a + X_ * b + c)[-1])/2).astype(int)
#     curve_cord_X = np.append(curve_cord_X,avg_x)
#     curve_cord_Y = np.append(curve_cord_Y,avg_y)

#     #print(X_[-1])
#     #print(Y_[-1])

# print(curve_cord_X)
# print(curve_cord_Y)
# X_AVG_val = np.mean(curve_cord_X)
# Y_AVG_val = np.mean(curve_cord_Y)

# center = [X_AVG_val, Y_AVG_val]

# # plt.plot(curve_cord_X, curve_cord_Y)
# plt.scatter(X_AVG_val, Y_AVG_val)


# # curve_coord_X = [147 147 162 162 187 187 212 212 237 237 262 262 282 282]
# # curve_coord_Y = [621 628 617 632 616 635 615 638 616 639 616 640 622 634]
# res_coords = []
# for i in range(0,len(curve_cord_X)):
#     x = curve_cord_X[i]-X_AVG_val
#     y = curve_cord_Y[i]-Y_AVG_val
#     if x > 0 and y > 0:
#         th_ = 0
#     elif x < 0 and y > 0:
#         th_ = 90
#     elif x < 0 and y < 0:
#         th_ = 180
#     elif x > 0 and y < 0:
#         th_ = 270
#     r = math.sqrt(x**2 + y**2)
#     th = float(math.atan(x/y))
#     res_coords.append((r,th+math.radians(th_),i))

# res_arr = sorted(res_coords, key=lambda d: d[1])
# print(res_arr)

# X__s = np.array(len(res_arr), dtype=int)
# Y__s = np.array(len(res_arr), dtype=int)

# for i in range(0,len(res_arr)):
#     # X__s = np.append(X__s, int(res_arr[i][0] * math.cos(res_arr[i][1])))
#     # Y__s = np.append(Y__s, int(res_arr[i][0] * math.sin(res_arr[i][1])))
#     X__s = np.append(X__s, curve_cord_X[int(res_arr[i][2])])
#     Y__s = np.append(Y__s, curve_cord_Y[int(res_arr[i][2])])

# plt.plot(X__s, Y__s)