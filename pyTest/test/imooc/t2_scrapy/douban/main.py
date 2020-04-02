#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------------------------------
# File Name: main.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-3-20-下午11:27
#---------------------说明--------------------------
#  启动工程.
#---------------------------------------------------

from scrapy import cmdline
cmdline.execute('scrapy crawl douban_spider'.split())

