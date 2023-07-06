import cv2
import os

# !/usr/bin/env python
# -*-coding:utf-8-*-
import cv2
import os
from PIL import Image

path = 'DIC-C2DH-HeLa-Train/DIC-C2DH-HeLa/01'
fsp = 3
fourcc = cv2.VideoWriter_fourcc(*'avc1')
video_path = './hecheng1.mp4'
video_out = cv2.VideoWriter(video_path, fourcc, fsp, (512, 512))

img_path = "DIC-C2DH-HeLa-Train/DIC-C2DH-HeLa/01/"
for i in range(0, 85):
    if i < 10:
        if os.path.exists(img_path + "t00" + str(i) + '.tif'):
            frame = cv2.imread(img_path + "t00" + str(i) + '.tif')
            video_out.write(frame)
    else:
        if os.path.exists(img_path + "t0" + str(i) + '.tif'):
            frame = cv2.imread(img_path + "t0" + str(i) + '.tif')
            video_out.write(frame)


video_out.release()
