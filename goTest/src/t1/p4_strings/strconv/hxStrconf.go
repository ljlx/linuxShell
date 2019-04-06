/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: main.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-6-下午7:50
---------------------说明--------------------------
 strconv包练习.
---------------------------------------------------
*/

package strconv

import (
	"strconv"
	"fmt"
	"os"
	"log"
	"bufio"
	"strings"
	"io"
)

func case1() {
	for _, truth := range []string{"1", "t", "TRUE", "false", "F", "0", "5"} {
		if b, err := strconv.ParseBool(truth); err != nil {
			fmt.Printf("\n{%v}", err)
		} else {
			fmt.Print(b, " ")
		}
	}
	fmt.Println()
}

func case2() {
	//	quote, 使用go语言双引号字符串语法形式来表示一个字符串.
	//	输出的是头尾带双引号的字符串.
	text1 := strconv.Quote("test旭旭")
	//同理,不过输出的是单引号
	text2 := strconv.QuoteRune('j')
	//"test\t\u65ed\u65ed\n"
	//相当于是转义
	text3 := strconv.QuoteToASCII("test\t旭旭\n")
	fmt.Println(text1, text2)
	fmt.Println(text3)
	//将其结果写入文件
	filename := "/tmp/test1"
	tfile := openfile(filename)
	tfile.WriteString(text3)
	tfile.Close()
	fmt.Println("写入文件[%s]完成.", filename)
	//	从文件读取结果并再次.输出
}

func case3() {
	tfile := openfile("/tmp/test1")
	tfileReader := bufio.NewReader(tfile)

	var strbuild strings.Builder
	for {
		line, isPrefix, err := tfileReader.ReadLine()
		if isPrefix {
			log.Fatalln("isPrefix:%s", isPrefix)
			return
		}
		if err != nil {
			if err == io.EOF {
				break
			}
			log.Fatalln(err)
			return
		}
		strbuild.Write(line)

	}
	filetext := strbuild.String()
	//反转义
	quoteText, _ := strconv.Unquote(filetext)
	fmt.Printf("原字符串[%s], strconv.Unquote: [%s] \n", filetext, quoteText)
}

func case4() {
	//	strconv.Atoi() （ASCII 转换成 int）
	asciiChars := "abc1234!@#$?AABBCC"
	//TODO 有没有办法在一个参数里面,直接使用多个返回值的方法
	atoichars, _ := strconv.Atoi(asciiChars)
	fmt.Printf("strconv.Atoi,字符串[%s]转int :[%d] ",
		asciiChars, atoichars)
	for _, item := range asciiChars {
		chartext := string(item)
		atoichars, _ := strconv.Atoi(chartext)
		fmt.Printf("strconv.Atoi,字符串[%s]转int :[%d] \n ",
			asciiChars, atoichars)
	}
}

func Teststrconv() {
	case1()
	case2()
	case3()
	case4()
}

func openfile(filename string) *os.File {
	var tfile *os.File
	var err error
	var operMode = os.O_CREATE | os.O_RDWR
	//var operPerm os.FileMode = 0700
	var operPerm os.FileMode = 0700
	if tfile, err = os.OpenFile(filename, operMode, operPerm); err != nil {
		log.Fatalf("create file stream has error")
	}
	return tfile
}
