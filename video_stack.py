import os
import sys
import glob
import ffmpeg
import cv2 as cv
import numpy as np

from shutil import move
from photo_stack import mk_stack_res

def mk_frames(filename, prefix='out_'):
    fmg = ffmpeg.input(filename).output('%s%%04d.png' % prefix)
    print(fmg.compile(), file=sys.stdout)
    fmg.run()

def mv_imgs(stacksize, path, f_prefix='_imgf'):
    files = glob.glob('*.png')
    # for idx in range(len(files)):
    idx = 0
    rng = int(len(files)/stacksize) + int(len(files)%stacksize)
    for i in range(rng):
        print(files[idx:idx+stacksize])
        dir_name = '%s_%s_%s' % (idx, idx+stacksize, f_prefix)
        full_path = f'{path}/{dir_name}'
        os.mkdir(full_path)
        try:
            for f in files[idx:idx+stacksize]:
                os.move(f, full_path)
        except OSError as e:
            print(e)
        mk_stack_res(full_path)
        idx+=stacksize

if __name__ == '__main__':
    in_video = sys.argv[1]
    path = in_video.split('/')[:-1]
    mk_frames(in_video)
    mv_imgs(10, path)

