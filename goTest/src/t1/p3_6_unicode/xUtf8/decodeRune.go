/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: decodeRune.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-7-上午9:33
---------------------说明--------------------------
 xUtf8测试练习
---------------------------------------------------
*/

package xUtf8

import (
	"unicode/utf8"
	"fmt"
)

func TestDecodeRune() {
	//返回str中头字符串的第一个码点及其字节数,或者U+FFFD(unicode替换字符串?)和0.
	//utf8.DecodeRuneInString()
	//同上,不过是最后一个
	//utf8.DecodeLastRuneInString()
	str := "Hello, 世界"
	for len(str) > 0 {
		r, size := utf8.DecodeRuneInString(str)
		fmt.Printf("%c %v\n", r, size)

		str = str[size:]
	}
}
