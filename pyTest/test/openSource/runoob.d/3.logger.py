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

logger = logging.getLogger("test")
logger.setLevel("DEBUG")
logger.info("info log")
logger.debug("debug log..")
logger.warn("warn log..")
logger.error("error log..")
