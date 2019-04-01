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

import "fmt"

func testForString() {
	//	一个 Go语言字符串是一个任意字节的常量序列
	//大部分情况下，一个字符串的字节使用UTF-8编码表示Unicode文本（详见上文中的“Unicode编码”一栏）。Unicode编码的使用意味着Go语言可以包含世界上任意语言的混合，代码页没有任何混乱与限制。
	//Go语言的字符串类型在本质上就与其他语言的字符串类型不同。Java的String、C++的std::string以及Python 3的str类型都只是定宽字符序列，而Go语言的字符串是一个用UTF-8编码的变宽字符序列，它的每一个字符都用一个或多个字节表示。
}

func testForRange(strs ...string) {
	for index, item := range strs {
		fmt.Println(index, item)

	}
}

func testString() {
	//1	Unicode编码字符,是utf-8的一个super, utf-8是一个unicode的子集
	//2 uhf-8编码,使用单字节(1符号位,7位)编码一个ascii的字符.
	//3 所有的ascii字符,在go中可以使用切片[]操作访问具体的一个字节.
	text0 := "hello"
	text1 := "hel我lo"
	//104 101 在ascii字码表上, 映射为 h和e, 验证了2和3.
	fmt.Println(text1[0], text1[1])
	//108 230 136 145 108. 在ascii字码表上是 字母'l' , 说明230 136 145 代表utf8编码下的'我'
	fmt.Println(text1[2], text1[3], text1[4], text1[5], text1[6], text1[7])
	//	-----------------------
	text2 := "hello,world"
	fmt.Printf("text[n]=%d,在字符串索引位置为n(utin8类型)处的{原始字节}. \n", text2[0])
	fmt.Printf("text[n:m]=%s,从位置n到位置m取得的{字符串}. \n", text2[0:5])
	fmt.Printf("text[:m]=%s,从索引位置0到位置m处取得的{字符串}. \n", text2[:len(text2)-1])
	fmt.Printf("字符串[%s]的字节数[%d] \n", text0, len(text0))
	fmt.Printf("字符串[%s]的字节数[%d] \n", text1, len(text1))
	//	多出的3个字节,就是那个 '我' 汉字
	char_a := 'a'
	char_b := 'b'
	char_c := 'c'

	fmt.Printf("字符ASCII : a=%d , b=%d , c=%d \n", char_a, char_b, char_c)
	fmt.Println("字符[a,b,c]的大小关系:", char_a < char_b, char_a < char_c, char_a < char_b)
	fmt.Println("字符[a,b,c]的大小关系:", char_a == char_b, char_a < char_c, char_a > char_b)
	fmt.Println("字符[a,b,c]的大小关系:", char_a-char_b, char_a+char_c, char_a*char_b)

}

func main() {
	fmt.Println("main start...")

	testForRange("test1", "test2", "test34", "test5")
	testString()

	fmt.Println("main end...")
}
