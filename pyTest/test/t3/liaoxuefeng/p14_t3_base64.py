#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p14_t3_base64.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-24-下午1:02
# ---------------------说明--------------------------
# base64
# ---------------------------------------------------
def base64Encode(text: str = 'hanxu'):
    """
    base64 编码字符串
    :param text:
    :return:
    """
    print("原文:", text)
    import base64
    encodeResult = base64.b64encode(text.encode())
    print("base64编码后:", encodeResult)
    return encodeResult


# base64Encode()

def base64Decode(base64Str: str):
    print("编码:", base64Str)
    import base64
    decodeResu = base64.b64decode(base64Str, validate=True)
    print("解码:", decodeResu)
    return decodeResu


if __name__ == '__main__':
    text = base64Encode('hanxu-hxjjj')
    base64Decode(text)
