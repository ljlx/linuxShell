#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p12-t5-distributedProcess.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-18-下午1:48
# ---------------------说明--------------------------
# 分布式进程.
# ---------------------------------------------------
# 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
#
# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
#
# 举个例子：如果我们已经有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
#
# 原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了。
#
# 我们先看服务进程，服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务：

import multiprocessing, logging, queue, threading, time

logging.basicConfig(level=logging.DEBUG, datefmt='%a, %d %b %Y %H:%M:%S', )

global gqueue  # 在使用前初次声明
gqueue = None  # 给全局变量赋值


# def obtainQueue() -> multiprocessing.Queue:
def obtainQueue() -> queue.Queue:
    global gqueue  # 再次声明，表示在这里使用的是全局变量，而不是局部变量
    if gqueue:
        logging.info("obtainQueue()==>已从cache获取队列:%s", id(gqueue))
        return gqueue
    else:
        l = threading.Lock()
        try:
            l.acquire()
            if gqueue:
                logging.info("obtainQueue()==>延迟获取队列成功:%s", id(gqueue))
                return gqueue
            else:
                gqueue = queue.Queue(5)
                logging.warning("obtainQueue()==>队列不存在,重新创建:%s", id(gqueue))
                return gqueue
        finally:
            l.release()


def jobProducter():
    queue = obtainQueue()
    logging.debug("jobProducter()==>生产者获得生产队列:%s", id(queue))
    import random, time
    logger = logging.getLogger("distributedProcess")
    while True:
        randomSleepTime = random.random()
        logger.debug("jobProducter()==>生产数据:%s", randomSleepTime)
        time.sleep(randomSleepTime)
        queue.put(randomSleepTime)


def threadProducter():
    logging.debug("producter()==>生产线程开始...")
    jobProducter()
    logging.debug("producter()==>生产线程完毕...")


def jobCustomer():
    mququq = obtainQueue()
    logging.debug("jobProducter()==>消费者获得消费队列:%s", id(mququq))
    while True:
        data = mququq.get()
        logging.debug("jobCustomer()==>消费数据:%s", data)


def threadCustomer():
    logging.debug("threadCustomer()==>消费线程开始...")
    jobCustomer()
    logging.debug("threadCustomer()==>消费线程完毕...")


def main_useThread():
    import threading
    tcus = threading.Thread(target=threadCustomer)
    tprod = threading.Thread(target=threadProducter)
    tcus.start()
    tprod.start()
    logging.info("main()==>启动生产/消费线程完毕.")

if __name__ == '__main__':
    main_useThread()



