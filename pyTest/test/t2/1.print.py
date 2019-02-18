#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: 1.print.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-12-下午4:07
# ---------------------说明--------------------------
# 关于输入日志功能的一些详细
# ---------------------------------------------------

print("abcd", "defgh", sep='-', end="--\t--\n--[ok]")

filestr = '/tmp/test.out'
logFileObj = open(filestr, mode='w+')
print("jjjjaaaa", file=logFileObj, flush=True)
logFileObj.flush()
# 不知什么原因,刚刚使用io对象写入的文件,不能使用相同的io对象读取.
# 经过验证,应该是因为 同一个io对象,对文件的位移有关,应该类似java的nio里的那个buffer对象
# logFileObj.seek(0)
print("日志文件内容:%s" % logFileObj.read())
with open(filestr, mode='r') as logfile:
    print("重新日志文件内容:%s" % logfile.read())
