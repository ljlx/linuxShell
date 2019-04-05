/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: switch.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-4-下午4:31
---------------------说明--------------------------
 switch测试练习
---------------------------------------------------
*/

package main

import (
	"fmt"
	"os"
	"bufio"
	"log"
	"strings"
)

/**

 */
func C1() {
	fmt.Println("开始进入")
	hxreader := bufio.NewReader(os.Stdin)
	var text string
	if byteText, isPrefix, err := hxreader.ReadLine(); err == nil {
		//fmt.Printf("开始解析 %d", byteText)
		//text = string(byteText)
		//fmt.Printf("%s", text)
		text = string(byteText)
		fmt.Printf("isPrefix:%t ,内容是:[%s] \n", isPrefix, )

	} else {
		//fmt.Println(isok)
		log.Fatal(err)
	}
	fmt.Printf("%s \n", text)
	switch text {
	case "hanxu":
		fmt.Printf("yes 猜对啦,我拼音是hanxu \n")
	case "韩旭":
		fmt.Printf("yes 猜对啦,我中文是hanxu \n")
	case "nihao":
		fmt.Printf("你好啊. \n")
	case "default":
		fmt.Printf("默认输出.继续匹配 \n")
		fallthrough
	default:
		fmt.Printf("我是默认输出. \n")
	}
}

func C2() {
	fmt.Println("请输入:")
	//inputtext := hxio.GetInputText()
	inputtext := "100,A"
	if inputtext != "" {
		//runestr := []rune(inputtext)
		fmt.Println("用户输入内容:", inputtext)

		argsArray := strings.Split(inputtext, ",")
		fmt.Printf("使用SplitAfter函数分隔,但是保留分隔符. %v", strings.SplitAfter(inputtext, ","))
		hellofilds := strings.Fields("hello")
		fmt.Println(hellofilds)
		//匿名函数也叫闭包
		helloTextArray := strings.FieldsFunc("hello,world hanxu;this is my.", func(r rune) bool {
			//fmt.Println(r)
			//执行了或运算
			//whatisit:=',' | ';' | ' '
			//fmt.Println(whatisit)
			switch r {
			case ',' , ';' , ' ':
				//fmt.Println("true")
				return true
			}
			return false
		})
		fmt.Printf("使用一个函数(使用多个分隔符)分隔字符串:%v \n", helloTextArray)
		//argsArray[0]
		marks := 1
		grade := string(argsArray[1])

		switch marks {
		case 90:
			grade = "A"
		case 80:
			grade = "B"
		case 50, 60, 70:
			grade = "C"
		default:
			grade = "D"
		}

		switch {
		case grade == "A":
			fmt.Printf("优秀!\n")
		case grade == "B", grade == "C":
			fmt.Printf("良好\n")
		case grade == "D":
			fmt.Printf("及格\n")
		case grade == "F":
			fmt.Printf("不及格\n")
		default:
			fmt.Printf("差\n")
		}
		fmt.Printf("你的等级是 %s\n", grade)
	} else {
		fmt.Printf("用户未输入内容\n")
		os.Exit(1)
	}

}

// switch 语句用于基于不同条件执行不同动作，每一个 case 分支都是唯一的，从上至下逐一测试，直到匹配为止。
//
//switch 语句执行的过程从上至下，直到找到匹配项，匹配项后面也不需要再加 break。
//
//switch 默认情况下 case 最后自带 break 语句，匹配成功后就不会执行其他 case，如果我们需要执行后面的 case，可以使用 fallthrough 。

func main() {
	method := C1
	// 如何设置一个集合list<func>

	method = C2
	method()
}
