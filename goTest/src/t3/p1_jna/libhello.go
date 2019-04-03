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
func HelloString(str string) *C.char {
	//TODO 返回值还是有问题的.
	//fmt.Println("ss")
	var buffer bytes.Buffer
	buffer.WriteString("hi")
	buffer.WriteString(",")
	buffer.WriteString(str)
	buffer.WriteString(",world")
	result := buffer.String()
	cresult := C.CString(result)
	return cresult
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
	//参考自https://studygolang.com/topics/6025/comment/17780
	//fmt.Println(HelloString("hanxu"))
}
