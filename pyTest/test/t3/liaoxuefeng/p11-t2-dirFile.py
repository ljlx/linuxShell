#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p11-t2-dirFile.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-10-上午9:53
# ---------------------说明--------------------------
# 操作文件和目录
# ---------------------------------------------------

def getAbsPath(pathStr: str):
    import os
    path = os.path.abspath(pathStr)
    return path


def genDirWithParentDir(pathStr):
    import os
    joinresu = os.path.join(pathStr, 'testdir1', 'testdir2', 'testdir3')
    return joinresu


if __name__ == '__main__':
    pathtmp = getAbsPath("/tmp/pytest")
    pathPytestDir = genDirWithParentDir(pathtmp)
    print(pathPytestDir)
