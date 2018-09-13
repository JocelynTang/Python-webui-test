#coding=utf-8
import os


# 此文件用于创建指定文件夹，如果要创建的文件夹已经存在，则不做任何操作。一般用于在测试脚本中创建测试截图存放的文件夹
def make_path(path):
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
