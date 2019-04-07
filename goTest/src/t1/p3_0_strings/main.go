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

import (
	"fmt"
	"unicode/utf8"
	"strconv"
	"bytes"
	"strings"
	"unicode"
	strconv2 "t1/p4_strings/strconv"
)

func testForString() {
	//	一个 Go语言字符串是一个任意字节的常量序列
	//大部分情况下，一个字符串的字节使用UTFk-8编码表示Unicode文本（详见上文中的“Unicode编码”一栏）。Unicode编码的使用意味着Go语言可以包含世界上任意语言的混合，代码页没有任何混乱与限制。
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
	text3 := "a测a"
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
	fmt.Printf("字符串[%s]转换Unicode码点[%d] \n", text3, []rune(text3))
	//可以使用更快的
	fmt.Printf("更快的字符串[%s]的字符数[%d]", text3, utf8.RuneCountInString(text3))
	fmt.Printf("字符串[%s]的字节数[%d],字符数[%d] \n", text3, len(text3), len([]rune(text3)))
	fmt.Printf("字符串[%s]的原始字节切片数组[%d],无副本地字节转字符串[%s] \n", text3, []byte(text3), string([]byte(text3)))
	fmt.Printf("将任意类型的数字i:[%d],转成字符串[%s],假设i是一个Unicode码点. \n", 99, string(99))
	allAsciiChar := ""
	for i := 1; i <= 200; i++ {
		allAsciiChar += string(i)
	}
	fmt.Printf("从0-200的ascii字符集合:%s \n", allAsciiChar)
	fmt.Printf("数字 [%d],tostring()==> [%s] \n", 88, strconv.Itoa(88))
	fmt.Sprint(44)
	fmt.Sprintf("任意类型x的字符串表示,相当于tostring(),其调用了类型的String()方法,数字:[%d],返回值为:%s", 66, 66)

}

func testChar2String() {
	allchar := ""
	//var allchar2 []string = nil
	allchar_rune := []rune{'æ', 0xE6, 0346, 230, '\xE6', '\u00E6'}
	for _, char := range allchar_rune {
		fmt.Printf("[0x%X '%c'] \n", char, char)
		allchar += string(char)

	}
	fmt.Println(allchar)
	fmt.Println("##---------------------分隔符-------------------------")
	//虽然方便，但是使用+= 操作符并不是在一个循环中往字符串末尾追加字符串最有效的方式。
	//TODO 方式一: 一个更好的方式（Python程序员可能非常熟悉）是准备好一个字符串切片（[]string），然后使用strings.Join()函数一次性将其中所有字符串串联起来。
	// 如何将一个码点切片快速转成一个[]string,不用循环+=.
	//strings.Join(allchar2,)可迭代的一个string?
	//strings.Join(allchar_rune," ")
	str_charrune := string(allchar_rune)
	//strings.Join(str_charrune,"")
	fmt.Println(str_charrune)
	//方式二:  但在Go语言中还有一个更好的方法，其原理类似于Java中的StringBuilder。这里有个例子。
	var buffer bytes.Buffer
	for {
		if piece, ok := getNextValidString(); ok {
			buffer.WriteString(piece)
		} else {
			break
		}
	}

	fmt.Print(buffer.String(), "\n")

	fmt.Println("###testChar2String-------------------------分隔符-----------------")
	//使用字符串创建一个rune(码点)切片,
	//变量chars的类型为 []int32, 因为rune是int32的同义词.
	chars := []rune("hello,world")
	//	同时需要在解析过程中能查看前一个或后一个字符时会有用。相反的转换也同样简单，其语法为S:=string(chars)
	chars2str := string(chars)
	fmt.Println(chars2str)
	fmt.Println("###testChar2String-------------------------分隔符-----------------")
	phrase := "hi,旭旭.hi"
	fmt.Printf("序列号 rune码点 字符 字节信息\n")
	for index, itemRune := range phrase {
		//for...range循环在迭代时将UTF-8字节解码成Unicode码点（rune类型）
		//为了得到一串字节码，我们将码点（rune 类型的字符）转换成字符串（它包含一个由一个或者多个 UTF-8 编码字节编码而成的字符）。然后，我们将该单字符的字符串转换成一个[]byte切片，以便获取其真实的字节码
		//[]byte(string)转换非常快（O(1)）
		charbyte := []byte(string(itemRune))
		fmt.Printf("[%-2d], [%U],[%c],16进制[%X], [%d] \n", index, itemRune, itemRune, charbyte, charbyte)
		//fmt.Printf("index[%-1d],rune码点[%U],可读字符[%c],字节[%X] \n", index, itemRune, itemRune, charbyte)

	}
	fmt.Println("###testChar2String-------------------------分隔符-----------------")
	//TODO 这个index是相较于字节的位置.不是字符的位置.
	hiIndex := strings.Index(phrase, "hi")
	hiLatestIndex := strings.LastIndex(phrase, "hi")
	fmt.Printf("字符串[%s] hi首次出现index[%d], 最后一次[%d] \n", phrase, hiIndex, hiLatestIndex)
}
func getNextValidString() (string, bool) {

	return "", false
}

//字符串切片
func testStringSlice() {
	textStr1 := "hi.旭gg.ff"
	//
	tbytePoint_first := strings.Index(textStr1, ".")
	tbytePoint_latest := strings.LastIndex(textStr1, ".")
	//把一个textstr转成int32类型的码点.下面两个变量本质是一样的.
	chars_rune := []rune(textStr1)
	//chars_int32 := []int32(textStr1)
	for index, charitem := range chars_rune {
		fmt.Printf("字符位置[%d]-字符[%c] \n", index, charitem)
	}
	//	该行的第一个和最后一个字,一个简单的方式是这样写代码
	firstWord := textStr1[:tbytePoint_first]
	//TODO 这个+1的地方可能是有问题的.因为这个索引的位置是字节.如果
	latestWord := textStr1[tbytePoint_latest+1:]
	fmt.Printf("通过码点切片来获取第一个单词[字节位置%d]-[%s],最后一个单词[字节位置%d]-[%s]", tbytePoint_first, firstWord, tbytePoint_latest+1, latestWord)
	//		tbytePoint_first := strings.Index(textStr1, " ")//用空格是不对的.
	//应该用unicode.IsSpace代替空格写法.或者 LastIndexFunc
	//	tbytePoint_first := strings.IndexFunc(textStr1,unicode.IsSpace)
	//
	//	虽然这个实例可以用于处理空格以及所有 7 位的ASCII 字符，但是却不适于处理任意的Unicode空白字符如U+2028（行分隔符）或者U+2029（段落分隔符）
	//ttt, firstWord_str := utf8.DecodeRuneInString(firstWord)
	//println(firstWord_str,ttt)
}

func testStringSlice2() {
	//下面这个例子在以任意空白符分隔字的情况下都可以找出其第一个字和最后一个字。

	line := " år　tørt\u2028vær"

	i := strings.IndexFunc(line, unicode.IsSpace) // i == 3

	firstWord := line[:i]

	j := strings.LastIndexFunc(line, unicode.IsSpace) // j == 9
	//这个DecodeRuneInString函数的意义在,以utf8编码找出当前切片 以j索引起点的字节位置的字符,到这个字符,末尾字节的一个长度
	//比如说 '旭'这个字符有3个字节230 151 173
	//'h旭i' 的字节编码是 104 230 151 173 105
	//_, char_xu_size := utf8.DecodeRuneInString("h旭i"[1:])
	//_, char_xu_size := utf8.DecodeRuneInString("旭")
	//println(char_xu_size) == 3
	//代表这个这个字符的字节长度是3.所以在使用字节切片的时候,要考虑计算这个字节长度问题.
	//详细参考书中的k3.4
	_, size := utf8.DecodeRuneInString(line[j:]) // size == 3

	lastWord := line[j+size:] // j + size == 12

	fmt.Println(firstWord, lastWord) // 打印：rå vær

}

func main() {
	fmt.Println("main start...")

	testForRange("test1", "test2", "test34", "test5")
	testString()
	testChar2String()
	testStringSlice()
	testStringSlice2()
	strconv2.Teststrconv()
	fmt.Println("main end...")
}
