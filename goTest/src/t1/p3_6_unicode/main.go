/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: main.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-7-上午9:31
---------------------说明--------------------------
 switch测试练习
---------------------------------------------------
*/

package main

import (
	"t1/p3_6_unicode/xUtf8"
	"t1/p3_6_unicode/xUnicode"
)

func main() {
	xUtf8.TestDecodeRune()
	xUnicode.DoTestUnicode()
}
