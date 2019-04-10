#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: xclearMovieName.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-2-2-下午12:35
# ---------------------说明--------------------------
# 清理下载的电影文件名.
# ---------------------------------------------------

# 1.加载指定的各个目录.
# 2.z;
import os


def getCurDir():
    """
    获取程序执行调用时的目录.
    :return:
    """
    pwdstr = os.getcwd()
    return pwdstr


def initSearchDir():
    """
    查找需要改名的目录,并返回目录列表
    :return:
    """
    pydir = []
    # 1.手动添加搜索的目录
    pydir.append("/media/hanxu/d/TDDOWNLOAD")
    return pydir


# 数据过滤链.
def filterChain(movieList):
    """
    匹配需要清洗的链,规则匹配的返回true
    :return:
    """
    lastlist = movieList
    for keyname, filter in filterDict.items():
        lastlist = filter(lastlist)
        # print("使用过滤器[%s]进行数据清洗过滤." % (keyname))
    return lastlist


def handlerChain(movieList: list):
    """

    :param movieList:
    :return:
    """
    lastresult = movieList
    for name, handler in handlerDict.items():
        lastresult = handler(lastresult)
    return lastresult


filterDict = {}
handlerDict = {}


def initFilter():
    """
    使用面向过程方法编程.
    向过滤链添加后缀名过滤
    :return:
    """
    filterDict['suffix'] = filter_suffix
    handlerDict['rmbracket'] = handler_bracket
    handlerDict['rmpoint'] = handler_rmSpaceAndPoint

    # 1.手动加载过滤规则.


def filter_suffix(movieList):
    """
    过滤器-匹配后缀是,mkv,rmvb等
    :return:
    """
    # (.+.sh$)|(.+.py$)
    # .+.(py|sh)$
    import re
    re_suffix = re.compile(r'.+.(avi|mkv|mp4|rmvb|gpg)$')

    def dofilter(movie):
        filename = os.path.basename(movie)
        matchResult = re_suffix.match(filename)
        if matchResult:
            return True
        return False

    # 过滤链如果处理, 这里不使用list. 后续一并多个filter计算
    return list(filter(dofilter, movieList))


def handler_rmSpaceAndPoint(movieList: list):
    """
    删除文件名的空格和小数点.
    :param movieList:
    :return:
    """

    def dofileter(movie):
        filename = os.path.basename(movie)
        dirname = os.path.dirname(movie)
        if isinstance(filename, str):
            if filename.startswith('.'):
                filename = filename.replace('.', '', 1)
            filename = filename.replace(" ", "")
        return os.path.join(dirname, filename)

    return list(map(dofileter, movieList))


def handler_bracket(movielist: list):
    """
    移除电影天堂相关不需要的字符串.
    :param movielist:
    :return:
    """
    import re
    """
    该表达式匹配'[]'括号及其括号里的内容,支持同时存在多个元素.
    """
    # re_bracket = re.compile(r'(\[\w+\])|(\[.+\])')
    # re_bracket = re.compile(r'(\[\w+\])|(\[((\w+|\.+)+)\])')
    # 测试字符串:
    # [sss-www.dy2018.com]testBDttt.rmvb
    # [ssswww.dy2018.com]testBDttt.rmvb
    # [asdf]test.mkv
    # [.]test.mkv
    # [sss].moviename.[asdf]
    # [xxxwww.dygod.com].[xxxwww.dygod.com].fff.[ss.1024ss].rmvb
    # [xxxwww.dygod.com]fff[ss.1024ss].rmvb
    re_bracket = re.compile(r'(\.?\[((\w+|\.+|\-+)+)\])')

    def mapfun(movie: str):
        filename = os.path.basename(movie)
        pathname = os.path.dirname(movie)
        # if "最后的武士" in movie:
        #     print("")
        #     pass
        bracketResult = re_bracket.finditer(filename)
        if bracketResult:
            for item in bracketResult:
                if isinstance(item, tuple):
                    for item2 in item:
                        filename = filename.replace(item2, "")
                elif isinstance(item, str):
                    filename = filename.replace(item, "")
                elif isinstance(item, re.Match):
                    filename = filename.replace(item.group(0), "")
            # print("文件 %s ==> %s" % (originalName, movie))
        return os.path.join(pathname, filename)

    return list(map(mapfun, movielist))


def init():
    initFilter()


def fullPathDir(dirTree, pathdir: str = '.'):
    curdirlist = os.listdir(pathdir)
    for item in curdirlist:
        parentdirs = os.path.join(pathdir, item)
        if os.path.isdir(parentdirs):
            fullPathDir(dirTree, parentdirs)
        else:
            dirTree.append(parentdirs)
    return dirTree


class fileTree(object):
    def __init__(self, originalName):
        """
        构造文件系统树对象.
        :param originalName: 名称
        :param fileOrDir: true:文件, false:目录
        """
        self.originalName = originalName
        self.changeName = originalName
        # self.fileOrDir = fileOrDir
        self._parseInit()

    def _parseInit(self):
        originalName = self.originalName
        self.isfile = os.path.isfile(originalName)
        self.index = 0
        self.isdir = os.path.isdir(originalName)
        if self.isfile:
            filestatus = os.stat(originalName)
            self.fileSize = filestatus.st_size
        elif self.isdir:
            self.subFileList = []
            self.subDirTree = []
            self.searchFile()

    def addFile(self, filepath):
        # test = os.lstat(filepath)
        # fileattr = os.stat(filepath)
        if self.isfile:
            raise BaseException('file obj no support addFile()')
        elif self.isdir:
            if isinstance(filepath, str):
                # self.fileLength = fileattr.st_size
                self.subFileList.append(fileTree(filepath))
                pass
            elif isinstance(filepath, fileTree):
                self.subFileList.append(filepath)
                pass
            return self

    def addDir(self, fileDir):
        if isinstance(fileDir, str):
            filetreeobj = fileTree(fileDir)
            self.subDirTree.append(filetreeobj)
        elif isinstance(fileDir, fileTree):
            self.subDirTree.append(fileDir)
        return self

    def searchFile(self):
        """
        递归搜索文件
        :return:3333
        """
        if self.isdir:
            self._recursiveSearch(self.originalName)
            pass
        elif self.isfile:
            raise BaseException('file obj not support this function.')
        s = self.originalName

    def _recursiveSearch(self, filepath=None):
        """
        递归方法->搜索目录及其文件.
        :return:
        """
        if filepath:
            for item in os.listdir(filepath):
                itempath = os.path.join(filepath, item)
                itemTree = fileTree(itempath)
                # print(itemTree)
                if itemTree.isdir:
                    self.addDir(itemTree)
                elif itemTree.isfile:
                    self.addFile(itemTree)
                # if itemTree and itemTree.isdir:
                # isfile=os.path.isfile(item)
                # isdir=os.path.isdir(item)


def mainTest():
    init()
    curdir = getCurDir()
    originalFileList = fullPathDir(pathdir=curdir)
    curdir = os.path.curdir
    # filelist =
    filterlist = filterChain(originalFileList)
    handlerResult = handlerChain(filterlist)
    for item in handlerResult:
        print(item)


def test():
    print("我是api测试")
    print(__file__)
    print("当前:%s", (os.getcwd()))
    filepath=os.getcwd()
    if not filepath:
        filepath = "/media/hanxu/Movie_And_Music/allMovie/rmvb"

    # filetreeobj = fileTree(os.getcwd())

    filetreeobj = fileTree(filepath)

    # filetreeobj.addFile(__file__)
    filetreeobj.addDir("/media/hanxu/Movie_And_Music/allMovie/rmvb")
    print(filetreeobj)

    def json2obj(x):
        print(x)
        return x['originalName']
        # pass

    try:
        import json
        print(json.dumps(filetreeobj, default=lambda x: x.__dict__))
        sss = json.loads(json.dumps(filetreeobj, default=lambda x: x.__dict__)
                         , object_hook=json2obj)
        print("ss")
    except BaseException as ex:
        print(ex)

    # filetreeobj.add


if __name__ == '__main__':
    test()
