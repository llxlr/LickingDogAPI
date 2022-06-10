#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import File, UploadFile
from PIL import Image
from cv2 import cv2
import base64
import glob
import os


async def img2base64(file_obj: UploadFile = File(...)):
    """image convert to base64"""
    if file_obj.filename != '':
        img = await file_obj.read()
        base64data = base64.b64encode(img)  # b64encode是编码
        await file_obj.close()
        return f'{base64data}'
        # <img src="data:image/jpg;base64,这里是base64的编码"/>


def base64_to_img(base):
    """base64 convert to image"""
    img_data = base64.b64decode(base)  # b64decode是解码
    return img_data


class Resolution(object):
    def __init__(self, img, save_path):
        self.img, self.save_path = img, save_path

    def single_image(self):
        """修改单张图片分辨率"""
        img = cv2.imread(self.img)   # 读取图片 rgb格式
        image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 格式转换，bgr转rgb
        image.save('qq1.jpg', quality=95, dpi=(300.0, 300.0))    # 调整图像的分辨率为300,dpi可以更改

    def multi_image(self):
        """批量修改图片分辨率"""
        img_path = glob.glob(self.save_path+"*.jpg")
        a = range(0, len(img_path))
        i = 0
        for file in img_path:
            name = os.path.join(self.save_path, "%d.jpg" % a[i])
            im = Image.open(file)
            im.thumbnail((178, 218))
            print(im.format, im.size, im.mode)
            im.save(name, 'JPEG')
            i += 1
