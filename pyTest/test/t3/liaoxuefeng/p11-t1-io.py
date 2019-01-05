#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p11-t1-io.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-5-上午9:33
# ---------------------说明--------------------------
# io操作
# ---------------------------------------------------

def readTextFile(strFile: str = None):
    if strFile == None or strFile.isspace():
        strFile = "/home/hanxu/document/project/code/personal/develop/linuxShell/pyTest/test/utils-py/debug.json"
    # ----------start----------测试文件打开数量上限----------start----------
    # 使用命令查看: ulimit -a 或者-n
    tryopenCount = 1
    fileList = list()
    # https://www.cnblogs.com/pangguoping/p/5791432.html
    # 查看当前这个文件打开数量
    # lsof -N /home/hanxu/document/project/code/personal/develop/linuxShell/pyTest/test/utils-py/debug.json |wc
    testFileLimit = False
    while testFileLimit:
        try:

            if tryopenCount % 100 == 0:
                print("本轮跳过.当前打开数量:{}".format(tryopenCount))
            fileitem = open(file=strFile, mode="r")
            fileList.append(fileitem)
            tryopenCount += 1
        except Exception as err:
            print(err)
            print("结束,共计打开文件数量:{}".format(tryopenCount))
            for item in fileList:
                item.close()
            raise err
            print("sss")
        finally:
            # 最后一步是调用close()方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：
            if False:
                fileitem.close()
    # 常见py异常类型如下.
    # https://docs.python.org/3/library/exceptions.html#exception-hierarchy
    # 总结
    #     每次使用try..except...finally file.close() 这种模板式代码太麻烦. py引入了with关键字来解决.
    # with open(file=strFile) as wFile:
    #     if wFile.readable():
    #         print(wFile.read())
    # ----------end------------测试文件打开数量上限----------end------------
    with open(file=strFile, mode='r') as wfile:
        # listLine = wfile.readlines()
        # print(listLine.__len__())
        outputtext = wfile.read()
        print("读取文件成功,", outputtext)


import codecs


def testByte():
    b = (b'python')
    barr = (b'p'b'y'b't')
    print(b)
    print(barr)
    print(b[0])
    # 我们可以用 b"*" 的形式创建一个字节类型，前提条件是这里的 * 必须是 ASCII 中可用的字符，否则将会超出限制
    # 那么问题来了，我们发现上面的 ASCII 表里面所有的字符只占据了 [31, 127]，那对于这一范围之外的数字我们要怎么才能表示为字节类型？答案就是用特殊的转义符号x+十六进制数字
    # [31,127] 之外的应该是一些控制字符,无法直接显示的
    # 0～31及127(共33个)是控制字符或通信专用字符（其余为可显示字符
    # 32～126(共95个)是字符(32是空格）,其中48～57为0到9十个阿拉伯数字。
    # 65～90为26个大写英文字母，97～122号为26个小写英文字母，其余为一些标点符号、运算符号等
    # https://baike.baidu.com/item/ASCII/309296?fr=aladdin
    print(b'xjjj')
    print(b'x24')
    print(b'xjjj'.__len__())
    byteData = bytes([66, 67, 68])
    print("字节转字符:", byteData)
    print("字节转16进制:", byteData.hex())
    print("从16进制转成字节对象,在以ascii打印", bytes.fromhex("6e 7a 7b 7c 7d 42"))
    print("从字符B转成字节,在转成16进制:", b'B'.hex())
    print("测试int的构造参数,int类型:", int(123456))
    print("测试int的构造参数,字符串类型:", int("123456"))

    print("测试int的构造参数,将字母B,转成16进制字符串,再以16进制解析该字符串为10进制的数字:", int(b'B'.hex(), base=10))
    print("测试int的构造参数,以10进制解析字符串[42]为10进制的数字:", int("42", base=10))
    print("测试int的构造参数,以16进制解析字符串[42]为10进制的数字:", int("42", base=16))
    allascii = []
    for i in range(32, 126):
        bytesi = bytes([i])
        allascii.append(str(bytesi))
        # print("字节位[{}],转译字符[{}],Hex[{}]".format(i, bytesi, bytesi.hex()))
    # print(allascii)


# https://www.imooc.com/video/8038 来自慕课网学习笔记
# python 文件打开的方式
# model     说明          注意
# r         只读方式打开      文件必须存在
# w         只写方式打开      文件不存在创建文件 & 文件存在则清空文件
# a         追加方式打开      文件不存在创建文件
# r+/w+     读写方式打开
# a+        追加和读写方式打开
# 以上任意一种追加b   为二进制方式打开. 比如 rb,wb,rb+ ab+...

def writeFile(file="/tmp/pytest/io.txt"):
    with open(file, mode='a') as wfile:
        if wfile.writable():
            wfile.write("test")
            wfile.writelines("testline")
            print("写入文件完成:", file)
            wfile.flush()


def readBinFile(file="/bin/ls"):
    with codecs.open(file, mode="rb") as rbinFile:
        rindexCount = 0
        while rbinFile.readable():
            rindexCount += 1
            # 自己想到的方式就是通过判断bls是否等于0,不过这个方式不好
            bls = rbinFile.read(4096)
            if rindexCount == 30:
                print()
            print("{},当前批次读取直接数:{}".format(rindexCount, bls.__len__()))
            # if isinstance(bls, bytes):
            #     for i in bls:
            #         print(i)


if __name__ == '__main__':
    print("开始测试")
    # readTextFile()
    # testByte()
    writeFile()
    # readBinFile()
# def file_like_objct():
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。
# file-like Object不要求从特定类继承，只要写个read()方法就行。
