package io

import (
	"os"
	"bufio"
	"io"
	"fmt"
	"strings"
	"bytes"
	"unicode"
	"unicode/utf8"
)

type testttt interface {
	test() string
}

func testInterfaceReader(reader io.Reader) {
	//b := []byte{1024}
	//reader.Read(b)
	return
}

func testreader(filename string) {
	if fileinput, err := os.Open(filename); err != nil {
		println(fileinput)
		bufreader := bufio.NewReader(fileinput)
		isloop := true
		for isloop {
			if linebyte, isPrefix, err2 := bufreader.ReadLine(); err2 != nil {
				println(isPrefix)
				println(linebyte)
			}
		}

	}

}

//从console从获取输入流
func GetInputText() string {
	bufinreader := bufio.NewReader(os.Stdin)
	if bytes, _, err := bufinreader.ReadLine(); err == nil {
		return string(bytes)
	}
	return ""
}

func DodeleteTest() {
	testText := "  Niccolò   • Noël• Geoffrey•Amélie• •Turlough•José  "
	fmt.Printf("对该字符串操作[%s]\n", testText)
	fmt.Printf("test func(%s),result: %s \n", "deleteSpaceChar1", deleteSpaceChar1(testText))
	fmt.Printf("test func(%s),result: %s \n", "deleteSpaceChar2", deleteSpaceChar2(testText))
	fmt.Printf("test func(%s),result: %s \n", "deleteSpaceChar3", deleteSpaceChar3(testText))
}

//对字符串处理,删除空白字符,第一种方式实现
func deleteSpaceChar1(text string) string {
	//unicode.包介绍?
	//去除头尾空格
	text = strings.TrimSpace(text)
	//strings.Fields()在字符串空白上进行分隔，返回一个字符串切片
	//// Some runes in the input string are not ASCII.
	//	return FieldsFunc(s, unicode.IsSpace)
	textarry := strings.Fields(text)
	text = strings.Join(textarry, "")
	return text
}

//我们还可以用bytes.Buffer来实现一种更加高效的空白处理方法
func deleteSpaceChar2(text string) string {
	splitchar := '#'
	splitcharLen := utf8.RuneLen(splitchar)
	var buffer bytes.Buffer
	//上一个是否是空白字符,多个连续空白字符保存一个就行
	//skip := true
	latestIsSpace := true
	for _, char := range text {
		if unicode.IsSpace(char) {
			if !latestIsSpace {
				buffer.WriteRune(splitchar)
				//skip = true
				latestIsSpace = true
			}
		} else {
			buffer.WriteRune(char)
			//skip = false
			latestIsSpace = false
		}
	}
	//以上处理多个连续空白字符,和隐式处理第一个空白字符,下面处理末尾空白字符.
	text = buffer.String()
	if latestIsSpace && len(text) > 0 {
		//这里可以使用-1个字节,是因为上面手动填写的是一个Ascii空白字符(空格),才可以-1
		//否则应该使用函数来正确获取连续的切割的字符串字节长度
		//utf8.RuneCountInString()取字符串(码点)的长度
		//utf8.DecodeRuneInString("") 取字符串字节的大小
		text = text[:len(text)-splitcharLen]
	}
	return text
}

//strings.Map()函数可以用来替换或者去掉字符串中的字符。
// 它需要两个参数，第一个是签名为func(rune) rune的映射函数，第二个是字符串。
// 对字符串中的每一个字符，都会调用映射函数，将映射函数返回的字符替换掉原来的字符，
// 如果映射函数返回负数，则原字符会被删掉
func deleteSpaceChar3(text string) string {
	isdelete := false
	var removeSpace = func(char rune) rune {
		isspace := unicode.IsSpace(char)
		if isspace {
			if isdelete {
				//删除该字符.
				return -1
			}
			return '#'
		}
		return char
	}
	text = strings.Map(removeSpace, text)
	return text
}
