#!/usr/bin/python3
# -- coding: utf-8 --
# --------------------------------------------------
# File Name: p8-t3-extend.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-10-23-下午10:16
# ---------------------说明--------------------------
# oop- 继承和多态
# ---------------------------------------------------

# ----------start----------这是父类声明----------start----------

class Animal(object):

    def __init__(self):
        self.name = '动物'

    def job(self):
        self.work = ''
        self.level = 0
        print("我不会工作,我的职称级别是:", self.level)

    def eat(self):
        self.food = '空气'
        print("我会吃[{}],但是不知道怎么吃".format(self.food))

    def get_name(self):
        return self.name

    def printInfo(self):
        log = "hi,i am {},i like eat {}, i can work {} with speed[{}]"
        log = log.format(self.name, self.food, self.work, self.level)
        print(log)


# ----------end------------这是父类声明----------end------------


# ----------start----------这是若干子类----------start----------
class Dog(Animal):
    pass


class Cat(Animal):
    def job(self):
        self.food = '鱼'
        self.work = '爬树,抓老鼠'
        self.level = 1
        print("我会 {},我的职称级别是:{}".format(self.work, self.level))


# ----------end------------这是若干子类----------end------------


# ----------start----------Main方法----------start----------

if __name__ == '__main__':
    animal1 = Animal()
    animal1Name = animal1.get_name()
    animal1.eat()
    animal1.job()
    animal1.printInfo()

    dog1 = Dog()
    dog1.job()
    # 奇怪的是,父类已经初始化的变量,food,level之类的,
    # 子类并没有继承,虽然使用上编译没有报错,但是如果使用一个未经子类初始化的父类定义的变量,子类和父类相关使用了其变量的代码块都会运行错误
    # AttributeError: 'Dog' object has no attribute 'food'
    # dog1.printInfo()

    cat1 = Cat()
    cat1.job()
    cat1.printInfo()
    # 判断一个变量是否是某个类型可以用isinstance()判断：
    print(isinstance(cat1, Cat))
    print(isinstance(cat1, Animal))
    print(isinstance(dog1, Animal))
    print(isinstance(dog1, Cat))
    print(isinstance(dog1, Dog))
    print(isinstance(dog1, object))

    classCat = type(cat1)
    import types


    def testFunc():
        print("this is test function type..")


    print(classCat)
    # 判断一个引用变量是不是函数类型,这个types包类似java的静态长量maybe
    # False
    print(type(cat1) == types.FunctionType)
    classCatJob = cat1.job
    # False
    print(type(classCatJob) == types.FunctionType)
    # False ,, why?,明明是一个函数啊.难道是因为在一个If判断里面写的原因吗
    print(testFunc == types.FunctionType)

    # True
    print(type(lambda x: x) == types.LambdaType)

    # True
    print(type((x for x in range(10))) == types.GeneratorType)

    # Pep8 do not compare types,ues isinstance
    # 能用type()判断的基本类型也可以用isinstance()判断

    # 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
    # True
    print(isinstance([1, 2, 3], (list, tuple)))
    # True
    print(isinstance((1, 2, 3), (list, tuple)))
    # 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
# ----------end------------Main方法----------end------------



