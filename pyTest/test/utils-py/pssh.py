#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: pssh.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-3-上午10:06
# ---------------------说明--------------------------
# 使用python来重写fssh.sh脚本
# ---------------------------------------------------
import json as xjson


# 可以参考跳板机源码

class sshConfig(object):

    def __init__(self):
        self.name = None
        self.code = None
        self.host = None
        # self.port = 22
        # self.addTime = xdate.today()
        self.identityFile = "~/.ssh/local.pri"
        self.keepAlive = True

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port: int):
        if port <= 0 or port >= 65536:
            raise ValueError("port must 1-65535,now is {}".format(port))
        self._port = port

    def tojson(self):
        # xjson.dumps(self, ensure_ascii=True)
        return xjson.dumps(self, default=lambda obj: obj.__dict__)


hk = sshConfig()
hk.name = "aliyun阿里-hk"
hk.code = "hk"
hk.host = "thesunboy.com"
hk.port = 1113
# print(hk.tojson())
strjson = xjson.dumps(hk, ensure_ascii=False, default=lambda obj: obj.__dict__)
print(xjson.dumps({'数字': 123, '字符': '一二三'}, ensure_ascii=True))
print(strjson)
