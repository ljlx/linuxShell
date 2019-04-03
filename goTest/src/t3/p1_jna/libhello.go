package main

import "C"
import (
	"fmt"
	"bytes"
)

//使用go build -buildmode=c-shared -o libhello.so ./libhello.go
//进行编译本地库.

//
//export Sum
func Sum(a int, b int) int {
	fmt.Println("ss")
	return a + b
}

//export HelloString
func HelloString(str string) string {
	//TODO 返回值还是有问题的.
	//fmt.Println("ss")
	var buffer bytes.Buffer
	buffer.WriteString("hi")
	buffer.WriteString(",")
	buffer.WriteString(str)
	buffer.WriteString(",world")
	result := buffer.String()
	return result
}

//export HelloString2
func HelloString2(str string) {
	//fmt.Println("ss")
	var buffer bytes.Buffer
	buffer.WriteString("hi")
	buffer.WriteString(",")
	buffer.WriteString(str)
	buffer.WriteString(",world")
	result := buffer.String()
	fmt.Println(result)
}

func main() {
	//fmt.Println(HelloString("hanxu"))
}
