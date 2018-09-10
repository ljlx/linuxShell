#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: img2char.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-9-7-下午12:39
# ---------------------说明--------------------------
# 图片转字符画,来源：https://www.shiyanlou.com/courses/370?utm_source=qq&utm_medium=social
# used img2char.py img.(jpg|png)
# ---------------------------------------------------
from PIL import Image
# argparse 库是用来管理命令行参数输入的
import argparse

# 列表-ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')  # 输出文件
parser.add_argument('--width', type=int, default=80)  # 输出字符画宽
parser.add_argument('--height', type=int, default=80)  # 输出字符画高
parser.add_argument('--log')

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output
islog = args.log
# TODO 作用？
unit = (256.0 + 1) / len(ascii_char)


# RGB值转字符的函数
# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '

    # gray：灰色。  不太明白这行是干嘛用的
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # 这两行 应该是取 这个像素点，要选用的字符，不知道是要以什么样的策略来决定这个显示的字符

    index = int(gray / unit)
    # 这个像素要显示的字符
    displayChar = ascii_char[index]
    if gray != 254 and islog is not None:
        log = "gray:[{0}],index[{1}],displayChar[{2}]".format(gray, index, displayChar);
        print(log)
    if gray == 254:
        displayChar = " "
    else:
        displayChar='+'
    return displayChar


if __name__ == '__main__':

    im = Image.open(IMG)
    # 应该是缩放图片，将图片按照NEAREST模式缩放成指定大小的图片，然后将图片色彩像素，转换成灰阶颜色的像素。
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
