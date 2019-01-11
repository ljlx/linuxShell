#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p12-t1-process.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-11-下午10:13
# ---------------------说明--------------------------
# 进程和多线程
# ---------------------------------------------------
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431927781401bb47ccf187b24c3b955157bb12c5882d000
# TODO python 多进程线程,提高篇.

def createSubProcess():
    """
    创建子进程
    Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
    :return: 子进程永远返回0，而父进程返回子进程的ID
    """
    import os
    print("main:当前进程id:{},当前父进程id:{}".format(os.getpid(), os.getppid()))
    subpid = os.fork()
    if subpid == 0:
        print("我是子进程,我的pid[{}], 我的ppid[{}]".format(os.getpid(), os.getppid()))
    else:
        print("我是父进程,我创建了一个子进程,其id是:{}".format(subpid))


#
# 由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！
#
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求
# 上面这段关于apache的说法是错的, 人家是采用进程+线程池实现


# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

def createSubProcessByModule():
    """
    由于使用系统os函数库,来fork子进程,只能在unix/linux系列计算机使用,无法跨平台.
    所以使用类库中提供的模块来跨平台的创建进程比较适合.
    :return:
    """
    from multiprocessing import Process
    import os
    # ----------start----------子进程run方法----------start----------
    def run_proc(name):
        print("run child process %s (%s)... " % (name, os.getpid()))
        print("child process end.")

    # ----------end------------子进程run方法----------end------------

    # ----------start----------主进程代码块----------start----------
    print("parent process %s." % os.getpid())

    def creSubpro(id: int):
        subprocess = Process(target=run_proc, name='subProcess-test', args=('test-' + str(id),))
        print("child process will start...")
        subprocess.start()
        return subprocess

    subprocessList = []
    for i in range(1, 10):
        msubprocess = creSubpro(i)
        subprocessList.append(msubprocess)

    print("sub process list:%s" % subprocessList)
    print("main process end.")
    # subprocess.join(timeout=10)
    # join()方法可以等待子进程结束后再继续往下运行

    # ----------end------------主进程代码块----------end------------


# Pool,
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程


if __name__ == '__main__':
    createSubProcessByModule()
