#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: 
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-10-20 下午12:38
# ---------------------说明--------------------------
#  自动化运维书第一章
# ---------------------------------------------------
# sudo apt-get install python-psutil python3-psutil python3-psutil-dbg  python-psutil-doc python-psutil-dbg

import psutil

virmem = psutil.virtual_memory()
radio = 1024 * 1024
print(virmem.total / radio)
print(virmem.active / radio)
print(virmem.available / radio)

cputim = psutil.cpu_times(True)

cpucount = psutil.cpu_count(logical=True)
print("cpu核数:", cpucount)
for item in cputim:
    print(item)

# disk info

# radio = 1000 * 1000
# it's is right disk info
hanxuuse = psutil.disk_usage(path='/home/hanxu/')
print(hanxuuse)
print(hanxuuse.free / radio)
d_disk = psutil.disk_usage(path='/media/hanxu/d/')
print(d_disk.free / radio)

diskpart = psutil.disk_partitions(False)
for item in diskpart:
    print(item)
diskio = psutil.disk_io_counters(False)
# diskiokey = diskio.keys()
# diskiovalue = diskio.values();

print(diskio)
print("磁盘io读取:{0}".format(diskio.read_bytes))
# for itemkey in diskio:
#     print(itemkey)
# 当前登陆用户
users = psutil.users()
for item in users:
    print(item)

# 当前开机时间

boottime = psutil.boot_time()
# linux时间搓表示
print(boottime)
import datetime

datetimeboot = datetime.datetime.fromtimestamp(boottime)
print(datetimeboot.strftime('%Y-%m-%d %H:%M:%S'))
print(datetimeboot)


def formattime(datetimeStamp: float):
    datetimeIns = datetime.datetime.fromtimestamp(datetimeStamp)
    return datetimeIns.strftime('%Y-%m-%d %H:%M:%S')


# 系统进程管理方法
ospids = psutil.pids()
print("当前进程数量:", len(ospids))
for itempid in ospids:
    itemprocess = psutil.Process(itempid)
    if itemprocess.name() == 'ping':
        print(itemprocess)
        print(itemprocess.cmdline())
        timestartStr = "启动时间:{0}".format(formattime(itemprocess.create_time()))
        print("线程数量:{0}".format(itemprocess.num_threads()))
        print(timestartStr)
        print(itemprocess.status())
    # print(itemprocess.kill())
args_list = ['/bin/ps']


