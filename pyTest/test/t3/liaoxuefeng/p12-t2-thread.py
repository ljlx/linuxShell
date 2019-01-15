#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p12-t2-thread.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-14-上午11:25
# ---------------------说明--------------------------
# 多线程.
# ---------------------------------------------------
# 多任务可以由多进程完成，也可以由一个进程内的多线程完成。
#
# 我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。
#
# 由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。
#
# Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
#
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行

import os
import threading
import time


# 新线程执行的代码:
def loop():
    print('thread, myPid[%s], ppid{%s} %s is running...' % (os.getpid(), os.getppid(), threading.current_thread().name))
    n = 0

    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def testThread():
    print("main pid[%s], ppid[%s]" % (os.getpid(), os.getppid()))
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()


print(threading.current_thread().name)

# 多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了

# def testSafeThread():
#     """
#     使用lock锁保证py线程安全, global,定义在函数内部,函数内部的内部函数, 使用会失败.name 'balance' is not defined
#     :return:
#     """
#     balance = 0
#
#     def change(n: int):
#         global balance
#         balance += n
#         balance -= n
#
#     def run(n):
#         for i in range(20):
#             change(i)
#
#     t1 = threading.Thread(target=run, args=(5,))
#     t2 = threading.Thread(target=run, args=(8,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print(balance)
# testSafeThread()

balance = 0


def change(n: int):
    global balance
    balance += n
    # import time
    # time.sleep(0.1)
    balance -= n


def run(n):
    for i in range(2000):
        if i % 200 == 0:
            import random, time, threading
            logf = []
            logf.append(threading.current_thread().getName())
            logf.append(i)
            logf.append(balance)
            logfTuple = tuple(logf)
            tu = ("s", 1, 1)
            print("currThread{},i:{}, balance:{}".format(threading.current_thread().getName()
                                                         , i, balance))
            time.sleep(random.randrange(1, 3))
        change(n)


def testSafeThread():
    for i in range(1, 10):
        t1 = threading.Thread(target=run, args=(9,))
        t1.start()


testSafeThread()

print(balance)
