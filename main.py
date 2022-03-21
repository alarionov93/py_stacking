from glob import glob
import sys
import numpy as np
import traceback
from PIL import Image

def mk_stack_res(dir_name):

	# when quality should not increase if we have more than 10, 100, 10000 photos?
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

	np_arr_modifyed = np.median(np_arr, 0)
	np_arr_converted = np_arr_modifyed.astype(np.uint8)

	img = Image.fromarray(np_arr_converted)
	return img

if __name__ == '__main__':
	try:
		mk_stack_res(sys.argv[1])
		img.save(('%sres_%s_%s.jpg' % (dir_name, imgs[0].split("/")[-1].split(".")[0], \
			imgs[-1].split("/")[-1].split(".")[0])), format="JPEG", subsampling=0, quality=100)
	except OSError as e:
	    print('OSError: can not save image.')
	except Exception as e:
		print('Unknown error. Exception was: %s' % str(traceback.format_exception(None, e, e.__traceback__)))

