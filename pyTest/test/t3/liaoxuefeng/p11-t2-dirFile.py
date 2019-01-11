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
    print("classpath:", os.getenv("CLASSPATH"))
    print("个人doc目录:", os.getenv("PERCDIR"))
    print("工作doc目录:", os.getenv("WORKDIR"))
    # print("全部环境变量:",os.environ)


def getAbsPath(pathStr: str):
    """
    获取指定目录,的物理路径
    :param pathStr:
    :return:
    """
    import os
    path = os.path.abspath(pathStr)
    return path


def debugErrorFunc(func, *obj):
    try:
        returnObj = func(*obj)
        return returnObj
    except BaseException as ex:
        print(ex)


def genDirWithParentDir(pathStr):
    import os
    # 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
    joinresu = os.path.join(pathStr, 'testdir1', 'testdir2', 'testdir3')
    # 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件
    splitResu = os.path.split(joinresu)
    print("分割路径:", splitResu)
    textxt = '/tmp/pytest/io.txt'
    print("分割得到路径文件的扩展名:", os.path.splitext(textxt))
    textxtDir = os.path.split(textxt)[0]
    textxtFile = os.path.split(textxt)[1]
    if not os.path.exists(textxtDir):
        os.mkdir(textxtDir)
    # os.write(,'testpy')TODO 第一个参数,文件描述符是个int.不太理解,难道是内存地址?
    # debugErrorFunc(os.write, textxtFile, "test py")
    # TODO os.renames() Q1:递归移动文件,但是有可能会遇到因种种情况(&权限,磁盘只读受限)而失败
    # 在这种情况下,移动文件结果会和系统保持一直嘛?
    # rename,需要注意移动的文件的路径问题,不能自由的像linux那样操作.
    os.rename(os.path.join(textxtDir, textxtFile), textxt + '.tmp')
    # 看文档,只能删除空目录,如果非空会异常,如果要删除目录树,需要使用
    # import shutil
    # shutil.rmtree()
    debugErrorFunc(os.rmdir, textxtDir)
    debugErrorFunc(os.remove, textxtDir)

    # tuple ('/tmp/pytest/io', '.txt')
    os.makedirs(joinresu, exist_ok=True)  # return None

    return joinresu


# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
#
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
# 其实也就是 sh-util-> 可能就是调用了系统封装的命令,而不是直接调用系统的原生函数

def listCurDir(dir='.'):
    """
    列表
    :param dir:
    """
    import os
    listAlldir = os.listdir(dir)
    listdir = [x for x in os.listdir(dir) if os.path.isdir(x)]
    print(listdir)


def findAllPyFile():
    import os
    filePyList = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
    print(filePyList)


if __name__ == '__main__':
    # pathtmp = getAbsPath("/tmp/pytest")
    # pathPytestDir = genDirWithParentDir(pathtmp)
    # print(pathPytestDir)
    # osInfo()
    listCurDir("/home/hanxu")
    findAllPyFile()
