#!/usr/bin/python3
# -*- coding: utf-8 -*-
#--------------------------------------------------
# File Name: p9-t1-mulitExtend.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-10-31-下午10:04
#---------------------说明--------------------------
# 多重继承
#---------------------------------------------------
# https://kevinguo.me/2018/01/19/python-topological-sorting/
# 一、什么是拓扑排序
#
# 在图论中，拓扑排序(Topological Sorting) 是一个 有向无环图(DAG,Directed Acyclic Graph) 的所有顶点的线性序列。且该序列必须满足下面两个条件：
#
# 每个顶点出现且只出现一次。
# 若存在一条从顶点A到顶点B的路径，那么在序列中顶点A出现在顶点B的前面。
# 它是一个DAG图，那么如何写出它的拓扑顺序呢？这里说一种比较常用的方法：
#
# 从DAG途中选择一个没有前驱(即入度为0)的顶点并输出
# 从图中删除该顶点和所有以它为起点的有向边。
# 重复1和2直到当前DAG图为空或当前途中不存在无前驱的顶点为止。后一种情况说明有向图中必然存在环。

# class A(object):
#     def foo(self):
#         print('A foo')
#     def bar(self):
#         print('A bar')
#
# class B(object):
#     def foo(self):
#         print('B foo')
#     def bar(self):
#         print('B bar')
#
# class C1(A,B):
#     pass
#
# class C2(A,B):
#     def bar(self):
#         print('C2-bar')
#
# class D(C1,C2):
#     pass
#
# if __name__ == '__main__':
#     print(D.__mro__)
#     d=D()
#     d.foo()
#     d.bar()



class A(object):
    def foo(self):
        print('A foo')
    def bar(self):
        print('A bar')

class B(object):
    def foo(self):
        print('B foo')
    def bar(self):
        print('B bar')

class C1(A):
    pass

class C2(B):
    def bar(self):
        print('C2-bar')

class D(C1,C2):
    pass

if __name__ == '__main__':
    print(D.__mro__)
    d=D()
    d.foo()
    d.bar()


# ----------start----------总结----------start----------
# 如果都需要使用拓扑排序来分析多重继承了，说明你系统类的继承体系设计有问题
# 当多继承的类中有相同的方法实现，同级的以取左原则，下级方法重写上级方法，感觉记住这个就行了
# 根据C3算法，第一次在某一父类中找到你需要调用的方法后就停止寻找
# ----------end------------总结----------end------------
