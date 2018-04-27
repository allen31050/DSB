import os
import cv2
import numpy as np

def rle_decoding(rle, H, W, fill_value=255):
    mask = np.zeros((H * W), np.uint8)
    rle = np.array([int(s) for s in rle.split(' ')]).reshape(-1, 2)
    for r in rle:
        start = r[0]-1
        end = start + r[1]
        mask[start : end] = fill_value
    mask = mask.reshape(W, H).T # H, W need to swap as transposing.
    return mask


acc = {}
with open('/Users/Allen/MEGA/DSB/mask-rcnn/data/__download__/stage1_solution.csv') as rle_file:
    next(rle_file)
    for line in rle_file:
        line_split = line.split(',')
        ID = line_split[0]
        rle = line_split[1]
        height = int(line_split[2])
        width = int(line_split[3])

        if ID in acc:
            acc[ID] += 1
        else:
            acc[ID] = 0
        dir_path = '/Users/Allen/MEGA/DSB/mask-rcnn/data/__download__/stage1_test/' + ID + '/masks/'
        if not os.path.exists(dir_path): os.mkdir(dir_path)
        mask_path = dir_path + str(acc[ID]) + '.png'
        print(mask_path)
        cv2.imwrite(mask_path, rle_decoding(rle, height, width))
