# -*- coding: utf-8 -*-
from fastapi import File, UploadFile
import base64


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
