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
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431954588961d6b6f51000ca4279a3415ce14ed9d709000#0
# ---------------------------------------------------
def base64Encode(text: str = 'han xu;'):
    """
    base64 编码字符串

    :param text:
    :return:
    """

    import base64
    btext = b''
    if isinstance(text, str):
        print("字符原文:", text)
        btext = text.encode()
    elif isinstance(text, bytes):
        print("字节原文:", text)
        btext = text
    encodeResult = base64.b64encode(btext)
    print("base64编码后(原始):", encodeResult)
    # # 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
    encodeResult_url = base64.urlsafe_b64encode(btext)
    print("base64编码(Url-save):", encodeResult_url)
    return encodeResult


# 如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用\x00字节在末尾补足后，再在编码的末尾加上1个或2个=号，表示补了多少字节，解码的时候，会自动去掉。

base64Encode()
base64Encode(b'i\xb7\x1d\xfb\xef\xff')
base64Encode(b'binary-i\xb7\x1d\xfb\xef\xff')

ss = 'woai你'.encode()
print(b'a'.hex())
print(int(b'a'.hex(), base=16))
def base64Decode(base64Str: str):
    print("编码:", base64Str)
    import base64
    decodeResu = base64.b64decode(base64Str, validate=True)
    print("解码:", decodeResu)
    return decodeResu


# 还可以自己定义64个字符的排列顺序，这样就可以自定义Base64编码，不过，通常情况下完全没有必要。
#
# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
#
# Base64适用于
# 小段内容的编码，
# 比如数字证书签名、Cookie的内容等。
#
# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：
# 去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串的长度变为4的倍数，就可以正常解码了。

if __name__ == '__main__':
    text = base64Encode('hanxu-hxjjj')
    base64Decode(text)
