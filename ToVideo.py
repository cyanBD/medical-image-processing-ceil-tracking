import cv2
import os

# !/usr/bin/env python
# -*-coding:utf-8-*-
import cv2
import os
from PIL import Image



def ToV(file_path, video_path):
    fsp = 10
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    video_out = cv2.VideoWriter(video_path, fourcc, fsp, (512, 512))
    for i in range(0, 85):
        if i < 10:
            if os.path.exists(file_path + "t00" + str(i) + '.tif'):
                frame = cv2.imread(file_path + "t00" + str(i) + '.tif')
                video_out.write(frame)
        else:
            if os.path.exists(file_path + "t0" + str(i) + '.tif'):
                frame = cv2.imread(file_path + "t0" + str(i) + '.tif')
                video_out.write(frame)
    video_out.release()

def ToV2(file_path, video_path):
    fsp = 5
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    video_out = cv2.VideoWriter(video_path, fourcc, fsp, (640, 480))
    for i in range(0, 85):
        if i < 10:
            if os.path.exists(r"track_res/man_track00" + str(i) + ".tif"):
                frame = cv2.imread(r"track_res/man_track00" + str(i) + ".tif")
                video_out.write(frame)
        else:
            if os.path.exists(r"track_res/man_track0" + str(i) + ".tif"):
                frame = cv2.imread(r"track_res/man_track0" + str(i) + ".tif")
                video_out.write(frame)
    video_out.release()


def ToV3(file_path, video_path):
    fsp = 6
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    video_out = cv2.VideoWriter(video_path, fourcc, fsp, (512, 512))
    for i in range(0, 18):
        if i < 10:
            if os.path.exists(file_path + "t00" + str(i) + '.jpg'):
                frame = cv2.imread(file_path + "t00" + str(i) + '.jpg')
                video_out.write(frame)
        else:
            if os.path.exists(file_path + "t0" + str(i) + '.jpg'):
                frame = cv2.imread(file_path + "t0" + str(i) + '.jpg')
                video_out.write(frame)
    video_out.release()

def ToV4(file_path, video_path):
    fsp = 6
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    video_out = cv2.VideoWriter(video_path, fourcc, fsp, (512, 512))
    for i in range(0, 18):
        if i < 10:
            if os.path.exists(file_path + "t00" + str(i) + '.tif'):
                frame = cv2.imread(file_path + "t00" + str(i) + '.tif')
                video_out.write(frame)
        else:
            if os.path.exists(file_path + "t0" + str(i) + '.tif'):
                frame = cv2.imread(file_path + "t0" + str(i) + '.tif')
                video_out.write(frame)
    video_out.release()


if __name__ == "__main__":
    ToV('DIC-C2DH-HeLa-Train/DIC-C2DH-HeLa/01/', "train1.mp4")
    ToV('DIC-C2DH-HeLa-Train/DIC-C2DH-HeLa/02/', "train2.mp4")
    ToV("exp66/", "jiance1.mp4")
    ToV2("", "track.mp4")
    ToV3("exp1/","res.mp4")
    ToV4('DIC-C2DH-HeLa-Train/DIC-C2DH-HeLa/01/', "res_to_compare.mp4")