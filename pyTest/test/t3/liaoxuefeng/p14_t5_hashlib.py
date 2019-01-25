#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p14_t5_hashlib.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-25-下午5:00
# ---------------------说明--------------------------
# hashlib,摘要算法简介.
# ---------------------------------------------------
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
#
# 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。
# 它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
# （通常用16进制的字符串表示）

import hashlib
import os


# TODO 获取当前运行的py文件名,和调用了当前py文件的
# 上下文环境,比如当本py文件被调用时,能取到调用时的所在路径,调用的py文件名.

def md5CurrPy():
    curPyFile = os.getcwd() + "/p14_t5_hashlib.py"
    md5obj = hashlib.md5()
    with open(curPyFile, mode='r+') as curPyFileIO:
        if curPyFileIO and curPyFileIO.readable():
            # TODO 如何判断io.readline()方法是否读取到最后一行数据了?
            loop = True
            indexCount = 0
            while loop:
                tmp = curPyFileIO.readline()
                if tmp:
                    print(tmp)
                    indexCount += 1
                    md5obj.update(tmp.encode())
                else:
                    loop = False
            md5value = md5obj.hexdigest()
            print("读取并计算文件md5结束.共计读取[%s]行,md5[%s]" % (indexCount, md5value))

md5CurrPy()