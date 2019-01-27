#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p14_t7_contextlib.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-26-下午9:02
# ---------------------说明--------------------------
# 探究with关键字以及使用contextmanager管理资源对象 
# ---------------------------------------------------
import pyTest.test.openSource.runoob.t3_logger as mylogger

logger = mylogger.getlogger("context")


# ----------start----------使用py语言原生实现----------start----------

class Testt(object):
    """this is test object for python """

    def __init__(self, num: int):
        self.mqueue = list()

    def __enter__(self):
        import os

        for item in os.listdir("./"):
            self.mqueue.append(item)
        logger.info("__enter__()==>初始化当前目录资源池完毕.共计[%s]个文件", len(self.mqueue))
        # 注意要返回一个对象,否则使用with无法得到这个对象.
        # return str("asdf")
        return self

    def returnObj(self, obj):
        q = self.mqueue
        q.append(obj)
        return True

    def pull(self):
        q = self.mqueue
        import random
        ranint = random.randint(1, 5)
        if ranint % 2 == 0:
            raise FileNotFoundError
        return q.pop()

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info("__exit__()==>开始释放资源池...")
        if exc_type:
            logger.info("__exit__()==>exec_type:%s", exc_type)
            logger.info("__exit__()==>exc_val:%s", exc_val)
            logger.info("__exit__()==>这是异常堆栈exc_tb:%s", exc_tb)
        # 2019-01-26 22:15:40 INFO __exit__()==>exec_type:<class 'FileNotFoundError'>
        # 2019-01-26 22:15:40 INFO __exit__()==>exc_val:
        # 2019-01-26 22:15:40 INFO __exit__()==>exc_tb:<traceback object at 0x7fa869dbc588>

        self.mqueue.clear()
        logger.info("__exit__()==>释放资源池完毕.")


def testWith():
    """

    :return:
    """
    with Testt(1) as te:
        tobj = te.pull()
        logger.info("testWith()==>%s", tobj)


# testWith()

# ----------end------------使用py语言原生实现----------end------------

# ----------start----------使用contextlib库来实现with语句----------start----------

# @contextmanager
#
# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：
from contextlib import contextmanager


class Testt2(object):

    def __init__(self, num: int):
        self.mqueue = list()

    def initfile(self):
        import os
        for item in os.listdir("./"):
            self.mqueue.append(item)

    def finishFile(self):
        self.mqueue.clear()

    def returnObj(self, obj):
        q = self.mqueue
        q.append(obj)
        return True

    def pull(self):
        q = self.mqueue
        import random
        ranint = random.randint(1, 5)
        if ranint % 2 == 0:
            raise FileNotFoundError
        return q.pop()


@contextmanager
def enterCreateQueue(size: int) -> str:
    logger.info("enterCreateQueue()==>创建队列,大小:%s", size)
    tinstance = Testt2(size)
    tinstance.initfile()
    # 这里可以实现从一个静态资源池,或者线程池,对接中间件等.
    yield tinstance.pull()
    tinstance.finishFile()
    print("释放资源池完毕.")


def testContextWith():
    with enterCreateQueue(10) as pyfile:
        logger.info("testContextWith()==>%s", pyfile)

# testContextWith()

# ----------end------------使用contextlib库来实现with语句----------end------------
# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

# 代码的执行顺序是：
#
# with语句首先执行yield之前的语句，因此打印出<h1>；
# yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 最后执行yield之后的语句，打印出</h1>。
#
# 因此，@contextmanager让我们通过编写generator来简化上下文管理


# ----------start----------自动关闭对象处理.----------start----------
# @closing
#
# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()

from contextlib import closing
from urllib.request import urlopen


@contextmanager
def myclosing(thing):
    try:
        yield thing
    finally:
        # 定义一个带@contextmanager装饰的上下文管理的函数。 例子中使用的对象的.close()方法，这要求调用的对象本身要有close方法才行

        thing.close()


def testClosing():
    with closing(urlopen("http://frp.thesunboy.com")) as page:
        for line in page:
            print(line)


def testMyClosing():
    """
    myclosing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单
    :return:
    """
    with myclosing(urlopen("http://frp.thesunboy.com")) as page:
        for line in page:
            print(line)


if __name__ == '__main__':
    """
    它的作用就是把任意对象变为上下文对象，并支持with语句。

@contextlib还有一些其他decorator，便于我们编写更简洁的代码
    """
    # testClosing()
    testMyClosing()

# ----------end------------自动关闭对象处理.----------end------------
