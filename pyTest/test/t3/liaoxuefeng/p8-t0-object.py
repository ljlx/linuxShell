#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: 
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-10-21 下午4:17
# ---------------------说明--------------------------
#  面向对象编程
# ---------------------------------------------------

std1 = {'name': 'Michael', 'score': 98}


def print_score(std):
    """
    打印学生分数信息
    :param std:
    """
    print('%s:%s' % (std['name'], std['score']))


print_score(std1)


# 以上是面向过程,下面是面向对象



class Student(object):
    mname = None
    mscore = None
    mlist = list()

    def __init__(self, name, score):
        self.mname = name
        self.mscore = score

    def append(self, stu):
        self.mlist.append(stu)

    def print_score(self):
        print('%s: %s' % (self.mname, self.mscore))
    def print_all(self):
        for item in self.mlist:
            item.print_score()


xiaomin = Student('hanxu', 99)
hx_1 = Student('hx_count', 99)
hx_2 = Student('hx_count2', 99)
hx_3 = Student('hx_count3', 99)

xiaomin.append(hx_1)
xiaomin.append(hx_2)
xiaomin.append(hx_3)

xiaomin.print_all()
