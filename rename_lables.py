# -*- coding: utf-8 -*-
import os

# 对所有文件以数字递增的方式重命名
def file_rename(r_path):
    i = 0
    # 需要重命名的文件绝对路径
    path = r_path
    # 读取该文件夹下所有的文件
    filelist = os.listdir(path)
    # 遍历所有文件
    for files in filelist:
        idx = files[-6:-4]
        file_name = "t0" + idx + ".txt"
        Olddir = os.path.join(path, files)
        Newdir = os.path.join(path, file_name)
        os.rename(Olddir, Newdir)
    return True


file_rename(r"G:\code\ML\DIC-C2DH-HeLa-Train\DIC-C2DH-HeLa\02_ST\lables")

