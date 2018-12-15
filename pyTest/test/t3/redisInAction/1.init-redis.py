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

print(redcli.get('key'))
print(redcli.get('s'))
keyvalue1 = redcli.get('key')
print(keyvalue1)
# 这是一个byte数组.

for item in keyvalue1:
    print(item)
keystr = str(keyvalue1)
print(keystr)

listtest1 = redcli.lrange('test1', 0, 20);
while True:
    for item in listtest1:
        print("redis:{%s}" % item)
    redcli.lpush('test1', item)
