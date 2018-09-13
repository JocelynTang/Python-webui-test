#coding=utf-8
import os


# 此文件用于读取指定路径下的某种类型文件的文件名，并返回文件名称
def get_filename(file_dir,file_type):
    F=[]
    for root,dirs,files in os.walk(file_dir,file_type):
        for file in files:
            if file.endswith(file_type):
                F.append(os.path.join(root,file))
        return F


# if __name__=='__main__':
#     file_dir='D:\Documents\Downloads'
#     files=get_filename(file_dir)
#     for file in files:
#         print file
        # if re.match(r'ALL-Config_\d{10}.tar.bz2',file):
        #     print 'OK'
        # else:
        #     print 'Failed'
        # os.remove(file)

