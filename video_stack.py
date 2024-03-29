import os
import sys
import glob
import ffmpeg
import subprocess
import cv2 as cv
import numpy as np

from shutil import move
from photo_stack import mk_stack_res, image_denoise, save_result_img
# for fixing quality issues add -vcodec libx265 -crf 24

STACK_VALUE = 2

def sort_by_num(x):
    return int(x.split('_')[1].split('.')[0])

def mk_frames(filename, prefix='out_', ext='.png'):
    if not os.path.isfile('%s0001%s' % (prefix, ext)):
        fmg = ffmpeg.input(filename).output('%s%%04d%s' % (prefix, ext))
        print(fmg.compile(), file=sys.stdout)
        fmg.run()
    else:
        print('Frames exists!')

def make_denoising(stacksize, path, f_prefix='imgf', use_stack=False):
    files = sorted(glob.glob('*.png'), key=sort_by_num)
    if not os.path.isfile(f'{path}/res_out_0001.jpg'):
        if use_stack == True:
            idx = 0
            rng = int(len(files)/stacksize) + int(len(files)%stacksize)
            # print(rng)
            for i in range(rng-1):
                try:
                    print(files[idx:idx+stacksize])
                    dir_name = '%s_%s_%s' % (idx, idx+stacksize, f_prefix)
                    full_path = f'{path}/{dir_name}'
                    # print(full_path)
                    os.mkdir(full_path)
                    for f in files[idx:idx+stacksize]:
                        move(f, full_path)
                        # print('move')
                except OSError as e:
                    print('1')
                    print(e)
                except IndexError as e:
                    print(e)
                idx+=stacksize

                # FIXME: stupid error -> not assigning result of function!!!
                res_frame, nn = mk_stack_res(full_path)
                save_result_img(res_frame, full_path, nn)
            print(f'{path}/*imgf')
            for d in sorted(glob.glob(f'{path}/*imgf'), key=lambda x: int(x.split('/')[-1].split('_')[0])):
                print(d)
                try:
                    files = glob.glob(f'{d}/res*.jpg')
                    f_name = files[0].split('/')[-1]
                    print(path)
                    subprocess.run(['mv', files[0], f'{path}/{f_name}'])
                except IndexError as e:
                    print(e)
                except OSError as e:
                    print(e)
        else:
            for f in files:
                print(f)
                res_frame, nn = image_denoise(f)
                save_result_img(res_frame, path, nn)
    else:
        print('Result frames exists!')


if __name__ == '__main__':
    use_stacking = True
    try:
        if sys.argv[2] == '1':
            use_stacking = False
            print('Not use stacking.')
    except IndexError:
        use_stacking = False
        print('Not use stacking.')

    in_video = sys.argv[1]
    v_name = in_video.split('/')[-1]
    path = in_video.split('/')[:-1]
    path = '/'.join(path)
    mk_frames(in_video)
    if use_stacking:
        stacksize = int(sys.argv[2])
    else:
        stacksize = STACK_VALUE
    make_denoising(stacksize, path, use_stack=use_stacking)

    # from this point - need to write on ffmpeg (but this way brakes the color) ? Or learn how to use libx265 with cv2 ?
    imgs = [cv.imread(x) for x in sorted(glob.glob(f'{path}/res*')) ]
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter(f'{path}/{v_name}_cv_test.mov', fourcc, 30, (1920,1080))
    for i in imgs:
        out.write(i)
    out.release()



