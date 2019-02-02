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


# 数据清洗链.
def filterChain(movieList):
    """
    清洗,规则匹配的返回true
    :return:
    """
    lastlist = movieList
    for keyname, filter in filterDict.items():
        lastlist = filter(lastlist)
        print("使用过滤器[%s]进行数据清洗过滤." % (keyname))
    return lastlist


filterDict = {}


def initFilter():
    """
    使用面向过程方法编程.
    向过滤链添加后缀名过滤
    :return:
    """
    filterDict['suffix'] = filter_suffix
    filterDict['rmbracket'] = filter_bracket
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
        matchResult = re_suffix.match(movie)
        if matchResult:
            return True
        return False

    # 过滤链如果处理, 这里不使用list. 后续一并多个filter计算
    return list(filter(dofilter, movieList))


def filter_bracket(movielist: list):
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

    def reduce(movie: str):
        originalName = movie
        if "最后的武士" in movie:
            print("")
            pass
        bracketResult = re_bracket.findall(movie)
        if bracketResult:
            for item in bracketResult:
                if isinstance(item, tuple):
                    for item2 in item:
                        movie = movie.replace(item2, "")
                elif isinstance(item, str):
                    movie = movie.replace(item, "")
            print("文件 %s ==> %s" % (originalName, movie))
        return movie

    return list(map(reduce, movielist))


def init():
    initFilter()


if __name__ == '__main__':
    init()
    curdir = getCurDir()
    filelist = os.listdir(curdir)
    filelist = filterChain(filelist)
    for item in filelist:
        print(item)
