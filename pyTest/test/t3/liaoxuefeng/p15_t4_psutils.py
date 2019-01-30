#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p15_t4_psutils.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-30-上午11:45
# ---------------------说明--------------------------
# psutil
# ---------------------------------------------------
# 用Python来编写脚本简化日常的运维工作是Python的一个重要用途。
# 在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，
# 如ps，top，free等等。要获取这些系统信息，
# Python可以通过subprocess模块调用并获取结果。
# 但这样做显得很麻烦，尤其是要写很多解析代码。
#
# 在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。
# 顾名思义，psutil = process and system utilities，
# 它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，
# 支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
import pkgutil
# import pyTest.test.t3.liaoxuefeng.p11_t1_io as myp11
import psutil


def testGetPkgimport():
    # myp11.mkdir("/tmp/asdf")
    # FileFinder 应该是类似java的classload的东西,用来寻找可导入的类库
    for item in pkgutil.iter_importers():
        # print(item)
        for item2 in pkgutil.iter_importer_modules(item):
            # print(item2)
            pass


def testGetCpuInfo():
    # psutil.test()
    print(" CPU逻辑数量:", psutil.cpu_count(logical=True))
    print(" CPU物理核心:", psutil.cpu_count(logical=False))
    print("times:", psutil.cpu_times())
    for x in range(3):
        # 百分比:percent
        # print(psutil.cpu_percent(interval=0.1,percpu=True))
        print(psutil.cpu_times_percent(0.1, True))


def testGetPids():
    print(psutil.Process(1).name())
    pids = psutil.pids()
    if pids:
        print("共计进程数:", len(pids))


def testGetPidByProcessName():
    pass


def testGetDiskInfo():
    print("磁盘使用情况:", psutil.disk_usage("/"))
    print("io计量:", psutil.disk_io_counters())
    print("磁盘分区信息:", psutil.disk_partitions())


def testGetNetInfo():
    from psutil import _common as pscommon
    netifinfo = psutil.net_if_addrs()
    if netifinfo and netifinfo['enp2s0']:
        ifenp2s0Info = netifinfo['enp2s0']
        print("有线网卡:", ifenp2s0Info)
    # print(netifinfo)
    connec = psutil.net_connections()
    for item in connec:
        if item.status == 'LISTEN':
            # print(item)
            pass
    listenIface = filter(lambda item: item.status == 'LISTEN', connec)
    # listenIface = filter(lambda item: item.laddr.ip == '0.0.0.0', listenIface)
    listenIfaceList = list(listenIface)
    for item in listenIfaceList:
        if isinstance(item, pscommon.sconn):
            # print(item)
            laddritem = item.laddr
            try:
                pidname = psutil.Process(item.pid).name()
                print("监听信息:[ %s ]- ip[ %s ]"
                      ",port[ %s ]"
                      ",pid:[ %s ]"
                      %
                      (pidname,
                       laddritem.ip,
                       laddritem.port,
                       item.pid))

            except BaseException as ex:
                print("无信息:", item)
                pass

    # print(connec)


def getBootTime():
    bootime = psutil.boot_time()

    from datetime import datetime
    currtime = datetime.now()
    print(bootime)
    print("启动时间:", datetime.fromtimestamp(bootime))
    print("当前时间:", currtime.strftime('%Y-%m-%d %H:%M:%S'))
    # print(datetime.)
    # datetime.strptime(str(currtime),'%Y')


def getMeminfo():
    pass


def getcurrVersion():
    print(psutil.version_info)


if __name__ == '__main__':
    # testGetPkgimport()
    # testGetCpuInfo()
    testGetNetInfo()
    # TODO 得注意版本信息, 不同版本的库结果会不一样.
    # getcurrVersion()
    # getBootTime()
    # testGetPidByProcessName()
    # testGetDiskInfo()
