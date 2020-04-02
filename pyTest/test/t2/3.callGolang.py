#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: 3.callGolang.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-4-4-下午3:28
# ---------------------说明--------------------------
# py调用go
# ---------------------------------------------------

linux_so_path = "/home/hanxu/document/project/code/personal/develop/linuxShell/goTest/src/t3/p1_jna/libhello.so"


def callgo():
    import ctypes
    import types
    libso = ctypes.CDLL(linux_so_path)
    if libso:
        print(type(libso))
        sumresult = libso.Sum(1, 5)
        print("py调用go静态库成功,其结果是 [%s]" % sumresult)
        # 调用字符串以及其他自定义类型需要解决.
        # print(libso.HelloString("iamhanxu"))
    else:
        print("无法使用go库")


if __name__ == '__main__':
    callgo()
