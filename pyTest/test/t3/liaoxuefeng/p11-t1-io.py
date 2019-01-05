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

def readFile(strFile: str = None):
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


if __name__ == '__main__':
    readFile()

# def file_like_objct():
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。
# file-like Object不要求从特定类继承，只要写个read()方法就行。
