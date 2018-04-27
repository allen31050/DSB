import os
import cv2
import numpy as np

DATA_DIR = '/Users/Allen/MEGA/DSB/mask-rcnn/results/mask-rcnn-se-resnet50-all/submit'
with open(DATA_DIR + '/sub-25k5.csv', 'r') as org_file:
	next(org_file)
	cur_ID = ''
	occupation = set()
	for mask in org_file:
		mask = mask.split(',')
		ID = mask[0]
		rle = mask[1]
		if ID != cur_ID:
			cur_ID = ID
			occupation = set()
		rle_split = rle.split()
		for n in range(int(len(rle_split) / 2)):
			for c in range(int(rle_split[2 * n + 1])):
				new_pixel = int(rle_split[2 * n]) + c
				if new_pixel in occupation:
					print(ID,":",new_pixel)
				else:
					occupation.add(new_pixel)
