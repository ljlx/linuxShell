#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: 1.argparser.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2018-12-20-下午3:03
# ---------------------说明--------------------------
#
# ---------------------------------------------------

import argparse
from builtins import int

_parser = argparse.ArgumentParser(description="this is my py script.")
_parser.add_argument('--arg1', type=str, default="test")
_parser.add_argument('--size', type=int, default=10)
_parser.add_argument('--max-size', type=int, default=10, required=True)
_parser.add_argument('--istest', type=bool, default=True)
pargs = _parser.parse_args()

# parser.add_argument 方法的type参数理论上可以是任何合法的类型， 但有些参数传入格式比较麻烦，
# 例如list，所以一般使用bool, int, str, float这些基本类型就行了，更复杂的需求可以通过str传入，
# 然后手动解析。bool类型的解析比较特殊，传入任何值都会被解析成True，传入空值时才为False

#
print("arg1-{},size-{},max-size-{},istest-{}".format
      (pargs.arg1, pargs.size, pargs.max_size, pargs.istest))
