import numpy as np

res = np.zeros((img.shape[0], img.shape[1]//2, 3), dtype=np.uint8)
x = 0
y = 0
for line in img:
    x += 1
    #print(len(line))
    for pix in range(img.shape[1]):
        #print(pix)
        if pix % 2 == 0:
            y += 1
            #print(pix)
            if y <= (img.shape[1]//2) - 1:
                p = (line[pix], line[pix+1])
                nn_p = []
                for i in range(3):
                    nn_p += [int((p[0][i] + p[1][i])/2)]
                #print(p)
                res[x][y] = nn_p