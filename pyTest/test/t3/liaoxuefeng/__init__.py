#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: 
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-08-25 下午1:13
# ---------------------说明--------------------------
#  
# ---------------------------------------------------
import os, logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s [%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )
logger = logging.getLogger("rename-py")


def findCurrDirPyFile(path=".") -> list:
    pylist = os.listdir(path)
    # [for item in pylist if os.path.isfile(item) and os.path.split(item)]
    pyfileNameList = []
    for item in pylist:
        isfile = os.path.isfile(item)
        filetext = os.path.splitext(item)
        if isfile and len(filetext) == 2:
            filename = filetext[0]
            fileSuffix = filetext[1]
            if ".py" == fileSuffix:
                pyfileNameList.append(filename + ".py")
    # print(pyfileNameList)
    return pyfileNameList


def dealWithPyList(pylist: list):
    for item in pylist:
        if isinstance(item, str):
            newpyname = item.replace("-", "_")
            logtext = "dealWithPyList()==>rename: [{}] -> [{}], result----[%s]".format(item, newpyname)
            logresult = "----[OK]"
            iserror = False
            try:
                result = os.rename(item, newpyname)
                logger.debug("dealWithPyList()==>" + logtext, result)
            except BaseException as ex:
                print(ex)
                logger.error("dealWithPyList()==>" + logtext, "Fail,the info:")


if __name__ == '__main__':
    pylist = findCurrDirPyFile()
    dealWithPyList(pylist)
