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
    defdict = defaultdict(default_factory=lambda: "defvalue")
    # defdict=defaultdict(lambda :"defvalue")
    defdict['id'] = 123
    defdict['name'] = 'namessss'
    print(defdict['names'])


getDefaultDict()
