#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: 2.untar.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-3-7-下午2:20
# ---------------------说明--------------------------
# 解压抽取文件测试
# ---------------------------------------------------
import tarfile as _tarfile
import os as _os


def tar(pakname='test.tar.gz'):
    pwd = _os.getcwd()
    print(pwd)
    t = _tarfile.open(pakname)

    # TODO 经过测试,确实只抽取解压出了这一个文件. 但是未验证性能,时候能不需要把整个压缩包加载到内存,或者是解压到了系统里了. 需要做大量小文件的压缩包测试
    t.extract('test/ooo', './')

    t.close()


tar()
