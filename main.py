from glob import glob
import sys
import numpy as np
import traceback
from PIL import Image

dir_name = sys.argv[1]

# recursive = sys.argv[2] or None
# if recursive:
# 	try:
# 		s_size = sys.argv[3]
# 	except IndexError:
# 		print("Stack size missing!")
path = '%s/*.jpg' % dir_name
imgs = glob(path)
print(path)

# get width and height
first_img = Image.open(imgs[0])
np_arr = np.zeros((len(imgs), first_img.size[1], first_img.size[0], 3))
idx = 0

for i in imgs:
	img = Image.open(i)
	np_arr[idx] = np.array(img)
	idx += 1

# print(np_arr)
# if recursive:
# 	np.linspace(0, len(files), num=s_size, dtype=np.uint8)
# 	for 
# 	np_arr[]

# when quality should not increase if we have more than 10, 100, 10000 photos?

np_arr_modifyed = np.median(np_arr, 0)
# np_arr_modifyed[np.where(np_arr_modifyed > 255)]
# np_arr_modifyed[np.where(np_arr_modifyed > 255)] = 255
# exit(0)
np_arr_converted = np_arr_modifyed.astype(np.uint8)

img = Image.fromarray(np_arr_converted)
try:
	img.save(('%sres_%s_%s.jpg' % (dir_name, imgs[0].split("/")[-1].split(".")[0], \
		imgs[-1].split("/")[-1].split(".")[0])), format="JPEG", subsampling=0, quality=100)
except OSError as e:
    print('OSError: can not save image.')
except Exception as e:
	print('Unknown error. Exception was: %s' % str(traceback.format_exception(None, e, e.__traceback__)))



