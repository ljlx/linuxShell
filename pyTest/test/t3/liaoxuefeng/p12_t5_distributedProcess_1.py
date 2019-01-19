#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p12-t5-distributedProcess-1.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-18-下午4:33
# ---------------------说明--------------------------
# 分布式进程学习-生产端-server
# ---------------------------------------------------
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431929340191970154d52b9d484b88a7b343708fcc60000#0

import pyTest.test.t3.liaoxuefeng.p12_t5_distributedProcess as myStep

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接受结果的队列.
result_queue = queue.Queue()


class MyQueueManager(BaseManager):
    pass


MyQueueManager.register('get_task_queue', callable=lambda: task_queue)
MyQueueManager.register('get_result_queue', callable=lambda: result_queue)

# 绑定端口5000, 设置验证码'abc':
manager = MyQueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()


# 获得通过网络访问的Queue对象:
def packagQueue(qu) -> queue.Queue:
    """
    请注意，当我们在一台机器上写多进程程序时，创建的Queue可以直接拿来用，但是，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，那样就绕过了QueueManager的封装，
    必须通过manager.get_task_queue()获得的Queue接口添加。
    :param qu:
    :return:
    """
    return qu


task = packagQueue(manager.get_task_queue())
result = packagQueue(manager.get_result_queue())

# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get()
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')
