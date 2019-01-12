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
# TODO 自定义代码规范规则: 以_开头定义内部函数
# 由于py支持 函数内部创建函数, 然后py又是使用缩进来代替括号,作为层级语法,
# 这样做会有一个问题:
# 1. 当在函数内,创建函数时,可能由于意外格式化代码,会造成创建的内部函数,被移动了外面,
# 2. 或者是外部的函数,被移动到了里面.
# 3.他们或者是自己长时间以后查看代码,不够理解这个层级结构,造成代码混乱.
# 所以我定一个规则
# 1.一个外部函数名,应该以小写字母开头,遵循驼峰命名(个人习惯,没遵守pip8规范.)
# 2. 任何内部函数名需要以'_'开头,内部函数的嵌套个数,定义该字符数量.

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
    def _run_proc(name):
        import time, random
        sleepSec = random.randint()
        print("run child process %s (%s)... " % (name, os.getpid()))
        time.sleep(sleepSec)
        print("child process end.")

    # ----------end------------子进程run方法----------end------------

    # ----------start----------主进程代码块----------start----------
    print("parent process %s." % os.getpid())

    def _creSubpro(id: int):
        subprocess = Process(target=_run_proc, name='subProcess-test', args=('test-' + str(id),))
        print("child process will start...")
        subprocess.start()
        return subprocess

    subprocessList = []
    for i in range(1, 10):
        msubprocess = _creSubpro(i)
        subprocessList.append(msubprocess)

    print("sub process list:%s" % subprocessList)
    print("main process end.")
    # subprocess.join(timeout=10)
    # join()方法可以等待子进程结束后再继续往下运行

    # ----------end------------主进程代码块----------end------------


# ----------start----------使用进程池来创建子进程----------start----------


def run_sub(id: int):
    """
    子进程运行的方法对象,类似于java的runable接口
    :param id:
    :return:
    """
    import os, time, random
    sleepTime = random.randrange(1, 4)
    print("subprocess-[%s],pid[%s] ,ppid[%s], is doing work.预计[%s]秒" % (id, os.getpid(), os.getppid(), sleepTime))
    time.sleep(sleepTime)
    if sleepTime % 3 == 0:
        print("subprocess-[%s] has error-1, now exit." % (id))
        # 第二个问题, 在其中一个子进程退出后,pool的父进程得不到响应,将一直因为join的原因 阻塞着,导致整个程序没有自然退出
        # exit(0)
    else:
        print("subprocess-[%s], ----done. exit..." % (id))


# Pool,
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
def createProcessWithPool():
    import os
    from multiprocessing import Pool
    # TODO 问题一: 需要了解内部函数的一些细节.为啥在Pool中,使用内部函数时,无法创建子进程.且不报错.
    # def run_sub(id:int):
    #     pass

    def _main():
        print("main process[%s],my parent process[%s]" % (os.getpid(), os.getppid()))
        # 使用4个子进程完成任务
        mypool = Pool(4)
        for i in range(1, 50):
            runarg = (i,)
            # 这个pool类似java线程池ThreadPoolExecutor,
            # 这个apply_async 类似java的submit方法向队列异步提交任务,然后4个子进程分别去共享队列拿item元素执行
            # TODO 看起来表现的和线程一样,不知有什么区别,和不同使用场景,记得线程的开销是远小于进程的开销
            runresult = mypool.apply_async(run_sub, args=runarg)
            # print("apply_async,结果:%s" % runresult)
        print("Waiting for all subprocesses done...")
        # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
        mypool.close()
        # mypool.apply_async(run_sub, args=(6,))#ValueError: Pool not running
        # TODO 问题二: 如果不join,父进程不等待子进程结果,退出了, 子进程也会直接退出.而不管子进程是不是执行完毕,可能是要考虑是否设置守护进程.
        #
        mypool.join()
        print('all subprocess done.')

    _main()


# ----------end------------使用进程池来创建子进程----------end------------

def useSubProcessWithModule():
    """
    很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
    subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
    :return:
    """
    import subprocess
    cmd = "nslookup"
    domain = "www.qq.com"
    print("$ %s %s" % (cmd, domain))
    r = subprocess.call([cmd, domain])
    while True:
        import time
        time.sleep(1)
        s = subprocess.call(["fremmina.sh"])
    print("exit code:", r)


if __name__ == '__main__':
    # import random
    # createSubProcessByModule()
    # print(type(random.random))
    # print(random.randrange(1, 5, step=1))
    # createProcessWithPool()
    useSubProcessWithModule()
