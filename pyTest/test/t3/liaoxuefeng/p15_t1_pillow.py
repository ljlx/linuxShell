#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p15_t1_pillow.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-27-下午1:17
# ---------------------说明--------------------------
# 第三方模块-图像处理库
# ---------------------------------------------------

from PIL import Image
from PIL.JpegImagePlugin import JpegImageFile

import pyTest.test.openSource.runoob.t3_logger as mylogger

logger = mylogger.getlogger("img")


def getImgObj(imgfile: str = None) -> JpegImageFile:
    """
    根据图片地址,打开图片管道流.
    :param imgfile:
    :return:
    """
    if not imgfile:
        return
    imgObj = Image.open(imgfile)
    logger.info("getImgObj()==>imgObj:%s", type(imgObj))
    return imgObj;


def hashImg(imgfile: str = None, hashtype=None):
    if not imgfile:
        return
    try:
        import pyTest.test.t3.liaoxuefeng.p14_t5_hashlib as myhashlib
        if not hashtype:
            hashtype = myhashlib.Hash_Type_SHA1
        hashsha = myhashlib.getHash(type=hashtype)
        with open(imgfile, mode='rb') as imgfileobj:
            imgbyte = imgfileobj.read()
            # read方法是直接读取所有内容.不在需要处理,读取末尾判断问题.但是如果是大文件,或者网络续传问题就不行了.
            # imgbyte2 = imgfileobj.read()
            # print("readable:", imgfileobj.readable())
            # print(len(imgbyte))
            # print(len(imgbyte2))
            hashsha.update(imgbyte)
            hexresult = hashsha.hexdigest()
        return hexresult
    except ImportError as err:
        print(err)


def getImgInfo(filePath: str):
    imgobj = getImgObj(filePath)
    # imgbyte=imgobj.tobytes()
    # if isinstance(imgbyte,bytes):
    #     logger.info("getImgSize()==>%s")
    logger.info("getImgSize()==>图像尺寸:%s", imgobj.size)
    logger.info("getImgSize()==>图像尺寸:%s,%s", imgobj.format, imgobj.format_description)
    # logger.info("getImgSize()==>图像信息:%s", imgobj.info)
    logger.info("getImgInfo()==>")


def doImgOper_thumbnail(filePath: str):
    imgobj = getImgObj(filePath)
    width, height = imgobj.size
    print("图片宽:%s,高%s." % (width, height))
    # thumbnail: 缩略图
    imgobj.thumbnail((width / 2, height / 2))
    print("图片缩放后的宽高:%s", imgobj.size)
    imgobj.show(title="图片缩放测试.")


#     其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
def doimgOper_fuzzy(filepath):
    from PIL import ImageFilter
    imgobj = getImgObj(filepath)
    # blur=fuzzy=模糊
    imgobj.filter(ImageFilter.BLUR) \
        .filter(ImageFilter.SMOOTH).show()


def createImg():
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    import random

    # 随机字母:
    def rndChar():
        return chr(random.randint(65, 90))

    # 随机颜色1:
    def rndColor():
        return (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

    # 随机颜色2:
    def rndColor2():
        return (random.randint(0, 255), random.randint(1, 255), random.randint(1, 255))

    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', 36)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字:
    # for t in range(4):
    #     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image = image.filter(ImageFilter.BLUR)
    image = image.filter(ImageFilter.BLUR)
    # https://pillow.readthedocs.org/
    image.show()


if __name__ == '__main__':
    imgfile = "/home/hanxu/picture/520.jpg"
    # print(hashImg(imgfile, 'md5'))
    # print(hashImg(imgfile, 'sha1'))
    # getImgInfo(imgfile)
    # doimgOper_fuzzy(imgfile)

    createImg()
