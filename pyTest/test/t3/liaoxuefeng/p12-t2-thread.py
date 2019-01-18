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
    import time
    time.sleep(0.0001)
    balance -= n


def run(n, lockobj: threading.Lock, isLock=True, ):
    for i in range(2000):
        # if i % 200 == 0:
        if balance != 0:
            import random, time, threading
            logf = []
            logf.append(threading.current_thread().getName())
            logf.append(i)
            logf.append(balance)
            logfTuple = tuple(logf)
            tu = ("s", 1, 1)
            print("错误数据:currThread{},i:{}, balance:{}".format(threading.current_thread().getName()
                                                              , i, balance))
            # time.sleep(random.randrange(1, 3))
        if isLock:
            lockobj.acquire()
            try:
                change(n)
            finally:
                lockobj.release()
                # pass
        else:
            change(n)


def testSafeThread():
    mlock = threading.Lock()
    for i in range(1, 10):
        t1 = threading.Thread(target=run, args=(i, mlock, True))
        t1.start()


def loopTest():
    """
    py由于gil锁的存在,无法实现真正的多线程.
    :return:
    """
    import multiprocessing
    cpucount = multiprocessing.cpu_count()
    print("cpu核心数量:", cpucount)

    def loop():
        while True:
            pass

    for i in range(cpucount):
        t = threading.Thread(target=loop())
        t.start()


loopTest()
# testSafeThread()

# 启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。
#
# 但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%，为什么Python不行呢？
#
# 因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。
#
# GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。
#
# 所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。
#
# 不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。

# TODO 上面介绍了Gil的概念, 不过也说了这是py默认的cpython解释器的问题,如果使用jpython应该没有这个问题.
# 参考下这个.
#  https://www.cnblogs.com/SuKiWX/p/8804974.html
# 不过看介绍,看来没那么简单啊, 主要是因为历史遗留问题,大量的库开发者,把python的对象当作是线程安全的.进行开发,
#
# 如果突然去掉gil, 可能会造成大量库代码多线程下会有问题.
# 之前也提到了既然GIL只是CPython的产物，那么其他解析器是不是更好呢？
# 没错，像JPython和IronPython这样的解析器由于实现语言的特性，他们不需要GIL的帮助。
# 然而由于用了Java/C#用于解析器实现，他们也失去了利用社区众多C语言模块有用特性的机会。
# 所以这些解析器也因此一直都比较小众。
# 毕竟功能和性能大家在初期都会选择前者，Done is better than perfect。
#
# 总结
#
# Python GIL其实是功能和性能之间权衡后的产物，它尤其存在的合理性，也有较难改变的客观因素。从本分的分析中，我们可以做以下一些简单的总结：
#
# 因为GIL的存在，只有IO Bound场景下得多线程会得到较好的性能
# 如果对并行计算性能较高的程序可以考虑把核心部分也成C模块，或者索性用其他语言实现
# GIL在较长一段时间内将会继续存在，但是会不断对其进行改进

print(balance)
