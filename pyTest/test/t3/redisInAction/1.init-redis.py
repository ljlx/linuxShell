#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: 1.init-redis.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2018-12-15-下午2:00
# ---------------------说明--------------------------
# redis-in-action 学习
# ---------------------------------------------------

from redis import Redis

redcli = Redis(host='localhost', port=10000)


def addRedisdata(redcli: Redis, nums):
    index = 1
    while index != nums:
        keystr = "test-{}".format(index)
        valuestr = "tvalue-{}".format(index)
        redcli.set(keystr, valuestr)
        index = index + 1


addRedisdata(redcli, 100 * 10000)
print(redcli.get('key'))
print(redcli.get('s'))
keyvalue1 = redcli.get('key')
print(keyvalue1)
# 这是一个byte数组.

for item in keyvalue1:
    print(item)
keystr = str(keyvalue1)
print(keystr)

listtest1 = redcli.lrange('test1', 0, 20)
redcli.zadd("testz", test=1, test2=2, test7=7, test5=5)
# while True:
#     for item in listtest1:
#         print("redis:{%s}" % item)
#     redcli.lpush('test1', item)
# print("使用阻塞版本的pop-api...")
# sdf = redcli.lpush("testblpop", "jjj", "kkk")
# print(sdf)
# resu = redcli.blpop(keys='testblpop', timeout=0)
print("使用阻塞版本的pop-api...取出数据:{}".format(resu))
