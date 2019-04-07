/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: xUnicode.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-7-下午4:31
---------------------说明--------------------------
xUnicode 测试练习
---------------------------------------------------
*/

package xUnicode

import (
	"unicode"
	"fmt"
	"strconv"
)

func jourgeUnicode() {
	//	判断一个字符是否属于一个特定的unicode分类,比如判断以下字符是否属于16禁止
	text := "abcxXfgh88o"
	fmt.Printf("\n字符\t\t是否十进制\t是否16进制 \n")
	for _, item := range text {
		fmt.Printf("[%s]\t %t \t\t %t \n", strconv.Quote(string(item)), IsDigit(item), IsHexDigit(item))
	}
}

// 判断字符是否 10进制数字
func IsDigit(rune2 rune) bool {
	return unicode.IsDigit(rune2)
}

// 判断字符是否 16进制数字
func IsHexDigit(rune2 rune) bool {
	//unicode.Is(table,c) //如果c在table中,返回true
	//unicode.IsControl(c)//如果c是一个控制字符,返回true
	//unicode.IsGraphic(c)//如果c是一个"图形"字符,即可显示为出人识别的图案,比如数字字母,标记符号空格,返回true
	//unicode.IsMark()//如果是一个标记,返回true
	//unicode.IsPrint()// 如果是一个可打印字符,返回true
	//unicode.IsPunct() // 如果是一个标点符号,返回true
	//unicode.IsSpace()//如果是一个空白字符('\t', '\n', '\v', '\f', '\r', ' ', U+0085 (NEL), U+00A0 (NBSP))
	//unicode.IsSymbol() // 如果是一个符号? what is 符号?
	//unicode.To(case,c)// 字符c的case版本,其中case可以是unicode.lowerCase,titlecase,or uppercase等等.

	return unicode.Is(unicode.ASCII_Hex_Digit, rune2)
}

func DoTestUnicode() {
	jourgeUnicode()
}
