/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: main.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-1-下午5:01
---------------------说明--------------------------
 main函数路口
---------------------------------------------------
*/

package main

func testForString() {
	//	一个 Go语言字符串是一个任意字节的常量序列
	//大部分情况下，一个字符串的字节使用UTF-8编码表示Unicode文本（详见上文中的“Unicode编码”一栏）。Unicode编码的使用意味着Go语言可以包含世界上任意语言的混合，代码页没有任何混乱与限制。
	//Go语言的字符串类型在本质上就与其他语言的字符串类型不同。Java的String、C++的std::string以及Python 3的str类型都只是定宽字符序列，而Go语言的字符串是一个用UTF-8编码的变宽字符序列，它的每一个字符都用一个或多个字节表示。
}

func testForRange(strs ...string) {
	for index, item := range strs {
		println(index, item)

	}
}

func main() {
	println("main start...")

	testForRange("test1", "test2", "test34", "test5")

	println("main end...")
}
