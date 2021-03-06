import os
import cv2

DATA_DIR = '../../data/__download__/'
for org_path in open('/Users/Allen/MEGA/DSB/mask-rcnn/data/split/test2_ids_color_220','r').readlines():
    filepath = org_path[:-1]
    train_test = filepath.split('/')[0]
    ID = filepath.split('/')[1]
    path = DATA_DIR + train_test + '/' + ID + '/images/' + ID + '.png'
    print(path)
    image = cv2.imread(path)
    os.rename(path, path[:-4] + "-bw.png")
    inv_image = (255 - image)
    cv2.imwrite(path,inv_image)
