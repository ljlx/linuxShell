#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: 3.logger.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-5-上午9:33
# ---------------------说明--------------------------
# logger操作学习
# ---------------------------------------------------
import logging

# https://blog.csdn.net/hallo_ween/article/details/64906838
#    logger：提供日志接口，供应用代码使用。
# logger最长用的操作有两类：配置和发送日志消息。
# 可以通过logging.getLogger(name)获取logger对象，
# 如果不指定name则返回root对象，
# 多次使用相同的name调用getLogger方法返回同一个logger对象。

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='myapp.log',
                    # filemode='w'
                    )
logger = logging.getLogger("test")
logger.setLevel("DEBUG")
logger.info("info log")
logger.debug("debug log..")
logger.warn("warn log..")
logger.error("error log..")

logging.info("logging.info")
logging.warning("logging.warning,%s", 12)
