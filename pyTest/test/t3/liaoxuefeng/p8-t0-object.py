#!/usr/bin/python3
# -- coding: utf-8 --
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

    def __init__(self, name, score):
        self.mname = name
        # 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
        # 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）
        # 只有内部可以访问，外部不能访问
        self.__privateName = name
        self.mscore = score
        self._test = True
        self.mlist = []
        # 需要注意的是，在Python中，变量名类似__xxx__的，
        # 也就是以双下划线开头，并且以双下划线结尾的，
        # 是特殊变量，特殊变量是可以直接访问的，不是private变量
        # ，所以，不能用__name__、__score__这样的变量名

    def get_privateName(self):
        return self.__privateName

    def append(self, stu):
        self.mlist.append(stu)
        stu.mname

    def print_score(self):
        print('%s: %s' % (self.__privateName, self.mscore))

    def __private_print_all(self):
        for item in self.mlist:
            item.print_score()

    def __print_all__(self):
        for item in self.mlist:
            item.print_score()


xiaomin = Student('hanxu', 99)
hx_1 = Student('hx_count', 99)
hx_2 = Student('hx_count2', 99)
hx_3 = Student('hx_count3', 99)

hx_1.mmmm = 9

print(hx_1.mmmm)

hx_1.mname

xiaomin.append(hx_1)
xiaomin.append(hx_2)
xiaomin.append(hx_3)

# xiaomin.__privateName 不能直接访问私有变量
# AttributeError: 'Student' object has no attribute '__privateName'
# print( xiaomin.__privateName)
print("私有变量访问:", xiaomin._Student__privateName)
xiaomin.__print_all__()

hx_1._test

# 有些时候，你会看到以一个下划线开头的实例变量名，
# 比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“
# 虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
#
# 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉
