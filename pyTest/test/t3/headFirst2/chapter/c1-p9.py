#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: c1-p9.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-8-25-下午5:56
# ---------------------说明--------------------------
# 模块介绍
# ---------------------------------------------------
# demo of 2
import datetime
import os
import sys

pwdstr = os.getcwd()
print(pwdstr)
os.system('sudo mkdir /test')
os.system("sudo virtualbox")
varkk = sys.version
llvar = sys.version_info
varkkk = sys.api_version
dfd = os.environ
fgdf = os.environb
jj = os.getenv("ll", "vv")
jjj = os.getenv("JAVA_HOME", "JAVAHO")
vark = os.getenv("JAVAHOME", "JAVAHO")

sss = datetime.datetime.today()
print(sss.year)
print(sss.month)

print(datetime.datetime.today().weekday())
print(datetime.datetime.today().minute)
print(sss.minute)

print(datetime.datetime.hour)

print(datetime.datetime.second)

print(datetime.datetime.day)
print(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
sss1 = datetime.datetime.isoformat(datetime.datetime.today())
print(sss)
print(sss1)
