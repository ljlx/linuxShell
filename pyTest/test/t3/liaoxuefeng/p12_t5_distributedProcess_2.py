#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p12_t5_distributedProcess_2.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-19-上午11:38
# ---------------------说明--------------------------
# 分布式进程学习-消费端-client
# ---------------------------------------------------
# 然后，在另一台机器上启动任务进程（本机上启动也可以）：

import time, sys, queue
from multiprocessing.managers import BaseManager


# import pyTest.test.t3.liaoxuefeng.p12_t5_distributedProcess_1 as myp12d1


# 创建类似的QueueManager:
class MyQueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
MyQueueManager.register('get_task_queue')
MyQueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = 'hk.thesunboy.com'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = MyQueueManager(address=(server_addr, 41000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
# task = myp12d1.packagQueue(m.get_task_queue())
# result = myp12d1.packagQueue(m.get_result_queue())
task = m.get_task_queue()
result = m.get_result_queue()

# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        # 多个work进程存在时,在结束时,get方法调用异常,无法正常退出进程.
        # 不是报empty异常.是报 raise EOFError错误.
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')
