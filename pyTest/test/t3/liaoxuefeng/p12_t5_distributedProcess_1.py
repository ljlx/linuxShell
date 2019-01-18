#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p12-t5-distributedProcess-1.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-18-下午4:33
# ---------------------说明--------------------------
# 分布式进程学习
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
