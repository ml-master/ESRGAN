import os
import re

# coding=utf-8
"""批量修改文件夹的图片名"""

import os
import time
from PIL import Image


# 批量修改图片尺寸，输入原图目录和修改后存放目录地址即可
def resize_batch(path, save_path):
    files = os.listdir(path)  # 返回path目录下的所有文件名

    # 遍历每一张图片并修改其尺寸
    for i in files:
        f = 0
        document = os.path.join(path, i)  # 返回path和i拼接之后的路径，即第i张图片
        img = Image.open(document)  # 读取第i张图片
        img_resize = img.resize((100, 128))  # 修改为100x128尺寸
        fileName = str(i)[:-4]  # 原图除后缀外的名字，这里原图后缀是.jpg
        img_resize.save(save_path + os.sep + '%s.png' % fileName)  # 保存路径，其中os.sep为系统分隔符


if __name__ == '__main__':
    dirPath = r"..\PyTorch\data\top_img"  ###添加自己的文件路径即可
    dirPath1 = r"..\PyTorch\data\top_img_1"  ###添加自己的文件路径即可
    # resize_batch(dirPath,dirPath1)
import os
from PIL import Image
import numpy as np

size_w, size_h = 512, 512  # 统一大小的宽高

# 提取目录下所有图片,更改尺寸后保存到另一目录
old_path = dirPath  # 原图片地址
new_path = r"..\PyTorch\data\img"  # 统一图片大小地址

for i in os.listdir(old_path):
    try:
        # 打开图像并将其调整为size_w x size_h大小
        old = os.path.join(old_path, i)
        new = os.path.join(new_path, i)
        img = Image.open(old).resize((size_w, size_h))
        # 将灰度图像转换为数组，并调整形状为(size_w, size_h,3)
        img_array = np.array(img).reshape((size_w, size_h, 3))
        # 保存形状为(size_w, size_h,3)的数组为图像
        img_new = Image.fromarray(img_array, mode='RGB')
        print(old, new)
        img_new.save(new)

    except Exception as e:
        print(old, e)
        continue
