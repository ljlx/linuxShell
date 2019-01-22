#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p14_t1_datetime.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-22-下午7:17
# ---------------------说明--------------------------
# datetime模块
# ---------------------------------------------------

from datetime import datetime, timedelta


def getdate(text: str = "asdf"):
    # print("input:", text)
    datenow = datetime.now().timestamp()
    nowstr = datetime.now().strftime('%Y-%m-%d')
    print(nowstr)
    print(datenow)


getdate("hello")


# str转换为datetime
#
# 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：

def inputTime():
    text = input(">")
    # 详细日期时间格式
    # https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    cday = datetime.strptime(text, '%Y-%m-%d %H:%M:%S')
    # 注意转换后的datetime是没有时区信息的。
    print(cday)


# datetime加减

# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：

def addtime(hours=0, days=0):
    currdate = datetime.now()
    return currdate + timedelta(days=days, hours=hours)


print("当前时间:", addtime())
print("时间加1天1小时:", addtime(1, 1))


# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
#
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：

def local2utcTime():
    from datetime import timezone
    currdate = datetime.now()
    print("当前时间:", currdate)
    print("时间函数2010-replace:", currdate.replace(year=2010))
    # delta: 河流的,so, timedelta, 时间流,时间长河?/xk
    # 创建时区UTC+8:00
    tzInfoUtc_8 = timezone(timedelta(hours=10))
    print("手动修改utc时间:", currdate.replace(tzinfo=tzInfoUtc_8))
    # datetime.datetime(2015, 5, 18, 17, 2, 10, 871012, tzinfo=datetime.timezone(datetime.timedelta(0, 28800)))
    # 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。


if __name__ == '__main__':
    local2utcTime()
