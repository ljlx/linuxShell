#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p14_t2_collections.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-22-下午8:01
# ---------------------说明--------------------------
# 
# ---------------------------------------------------


# 我们知道tuple表示不变集合.例如一个点的二维坐标如下表示.
def ppoint():
    """
     namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。

 可以验证创建的Point对象是tuple的一种子类
    :return:
    """
    from collections import namedtuple
    p = (1, 2)
    # 但是看到这个(1,2),很难让人理解这是一个坐标.
    # 这时我们不能想,那么可以用一个dict,甚至是class来表示,
    # 可是这不免又小题大做了.这时我们可以使用namedtuple
    Point = namedtuple("Point", ['x', 'y'])
    p2 = Point(1, 2)
    p2x = p2.x
    p2y = p2.y
    print("namedtuple创建的Point类型:%s, 值[%s]" % (type(p2), p2))
    print("Point实例类型判断:%s" % isinstance(p2, Point))
    print("Point是否Tuple类型:%s" % isinstance(p2, tuple))


def getCircle():
    """
    类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
    :return:
    """
    from collections import namedtuple
    circle = namedtuple('Circle', ['point_x', 'point_y', 'radius'])
    circle.point_x = 1
    circle.point_y = 1
    circle.radius = 1
    return circle


def testCircle():
    cir = getCircle()
    print(cir.point_x, cir.point_y, cir.radius)


# ppoint()
# testCircle()

# Deque双向队列.
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
#
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈

def getDeque():
    from collections import deque
    queue_double = deque(['a', 'b', 'c'])
    queue_double.append('zz')
    queue_double.appendleft('aa')
    # deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
    return queue_double


def testDeque():
    q = getDeque()
    z = q.pop()
    print(z)
    print(q.popleft())
    print(q)


# testDeque()
# defaultdict
#
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：

def getDefaultDict():
    from collections import defaultdict
    # default_factory不是关键字参数.
    # defdict = defaultdict(default_factory=lambda: "defvalue")
    defdict = defaultdict(lambda: "defvalue")
    defdict['id'] = 123
    defdict['name'] = 'namessss'
    print("字典所有值:", defdict)
    print("不存在的key:", defdict['names'])


def orderDict():
    """
    默认的dict是hash的,迭代key是不保证顺序的.使用OrderedDict可以保证key是顺序的
    :return:
    """
    from collections import OrderedDict
    dict1 = dict([('k1', 'v1'), ('k2', 'v2'), ('kk1', 'vv1'), ('kk2', 'vv2')])
    print(dict1)
    dict2 = OrderedDict(dict1)
    dict3 = OrderedDict([('k1', 'v1'), ('k2', 'v2'), ('kk1', 'vv1'), ('kk2', 'vv2')])
    print("排序字典(按照插入顺序):", dict3)
    print("排序字典(由dict对象转化而来,顺序有问题):", dict2)
    #     注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身自然排序


def chainDictMap():
    """
    ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，
    但是查找的时候，会按照顺序在内部的dict依次查找。
    什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，
    可以通过环境变量传入，还可以有默认参数。我们可以用ChainMap实现参数的优先级查找，
    即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数
    :return:
    """
    from collections import ChainMap
    import os, argparse

    defaultArg = {'user': 'hanxu', 'age': 20}
    # 构造命令行参数
    myargparse = argparse.ArgumentParser()
    myargparse.add_argument('-u', '--user', help="描述信息-用户名")
    myargparse.add_help
    myargparse.add_argument('-A', '--age')
    namespace = myargparse.parse_args()
    varsDictName = vars(namespace)
    print("vars(myargparse.parse_args()):", varsDictName)
    command_line_args = {k: v for k, v in vars(namespace).items() if v}
    print("命令参数:", command_line_args)
    print(namespace.user)
    #   组合成chainMap:
    #    osenv=os.environ
    comblined = ChainMap(command_line_args, defaultArg)
    print("最终形成类似springBoot的参数机制:", comblined)
    print("user:", comblined.get('user'))
    print("age:", comblined.get('age'))


def counter():
    """
    简单的计数器
    :return:
    """
    from collections import Counter
    mycounter = Counter()
    for item in 'hello,world':
        mycounter[item] += 1
    # count大于等于2,
    print(mycounter.most_common(2))
    print("排序:", sorted(mycounter))
    myitems = mycounter.items()
    myelement = mycounter.elements()
    sortitem = sorted(myitems)
    sortelement = sorted(myelement)
    print("".join(sorted(myitems)))

    print("".join(myelement))

    print("计数器:类型[%s] ,\n计数结果[%s]" % (type(mycounter), mycounter))


# getDefaultDict()
# orderDict()
# chainDictMap()
counter()
