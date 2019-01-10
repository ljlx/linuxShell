#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p11-t2-dirFile.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-8-下午5:40
# ---------------------说明--------------------------
# IO编程-操作文件和目录
# ---------------------------------------------------

def osInfo():
    """
    注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的
    :return:
    """
    import os
    # posix:linux,unix,MacOsX ,nt:window
    print(os.name)
    print(os.uname())
    osenv = os.environ
    osenv.
    print("classpath:", os.getenv("CLASSPATH"))
    print("个人doc目录:", os.getenv("PERCDIR"))
    print("工作doc目录:", os.getenv("WORKDIR"))
    # print("全部环境变量:",os.environ)


if __name__ == '__main__':
    osInfo()
