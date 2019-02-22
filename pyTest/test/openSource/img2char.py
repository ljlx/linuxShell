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
# argparse 库是用来管理命令行参数输入的

# 字符画是一系列字符的组合，我们可以把字符看作是比较大块的像素，一个字符能表现一种颜色（为了简化可以这么理解），字符的种类越多，可以表现的颜色也越多，图片也会更有层次感。
#
# 问题来了，我们是要转换一张彩色的图片，这么多的颜色，要怎么对应到单色的字符画上去？这里就要介绍灰度值的概念了。
#
#     灰度值：指黑白图像中点的颜色深度，范围一般从0到255，白色为255，黑色为0，故黑白图片也称灰度图像。
#
# 另外一个概念是 RGB 色彩：
#
#     RGB色彩模式是工业界的一种颜色标准，是通过对红(R)、绿(G)、蓝(B)三个颜色通道的变化以及它们相互之间的叠加来得到各式各样的颜色的，RGB即是代表红、绿、蓝三个通道的颜色，这个标准几乎包括了人类视力所能感知的所有颜色，是目前运用最广的颜色系统之一。- 来自百度百科介绍
#
# 我们可以使用灰度值公式将像素的 RGB 值映射到灰度值（注意这个公式并不是一个真实的算法，而是简化的 sRGB IEC61966-2.1 公式，真实的公式更复杂一些，不过在我们的这个应用场景下并没有必要）：
#
# gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b
#
# 这样就好办了，我们可以创建一个不重复的字符列表，灰度值小（暗）的用列表开头的符号，灰度值大（亮）的用列表末尾的符号。
import argparse

from PIL import Image

# 列表-ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# ascii_char=list("abcdefghijklmnopqrstuvwxyz/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
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
    elif gray == 107:
        displayChar = " "
    # else:
    #     displayChar='.'
    # else:
    #     displayChar='+'

    return displayChar


if __name__ == '__main__':

    im = Image.open(IMG)
    # 应该是缩放图片，将图片按照NEAREST模式缩放成指定大小的图片，然后将图片色彩像素，转换成灰阶颜色的像素。
    # Image.NEAREST，表示输出低质量的图片。
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
