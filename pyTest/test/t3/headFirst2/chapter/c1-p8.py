#!/usr/bin/python3
# coding=utf-8
# --------------------------------------------------
# File Name: c1-p8.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-8-25-下午1:16
# ---------------------说明--------------------------
# datetime-and-array
# ---------------------------------------------------

import time;
from datetime import datetime

# allMinuteNums = range(1, 60, 1);所有的，步进为1
allMinuteNums = range(1, 60, 2)
# for item in allMinuteNums:
# print(item)

for item in range(4):
    time.sleep(3)
    nowMinu = datetime.today().second
    if nowMinu in allMinuteNums:
        print("now minute is odd:", nowMinu)
    else:
        print("now minute is not odd,even:", nowMinu)
