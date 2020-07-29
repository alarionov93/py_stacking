from glob import glob
import sys
import numpy as np
from PIL import Image

dir_name = sys.argv[1]

imgs = glob('./%s/*.jpg' % dir_name)

# get width and height
first_img = Image.open(imgs[0])
np_arr = np.zeros((len(imgs), first_img.size[1], first_img.size[0], 3))
idx = 0

for i in imgs:
	img = Image.open(i)
	np_arr[idx] = np.array(img)
	idx += 1

print(np_arr)

np_arr_modifyed = np.mean(np_arr, 0)

np_arr_converted = np_arr_modifyed.astype(np.uint8)

img = Image.fromarray(np_arr_converted)
try:
	img.save('test_img.jpg', "JPEG")
except OSError as e:
    print('OSError: can not save image.')
except Exception as e:
	print('Unknown error.')



