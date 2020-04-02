/*
--------------------------------------------------
 File Name: TestMain.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-29-上午11:12
---------------------说明--------------------------
 main
---------------------------------------------------
*/

package main

import (
	"bufio"
	"log"
	"net"
	"os"
	"reflect"
	"t3/p4_terminal/t1_session"
	"t3/p4_terminal/t2_tcpnet/case1"
)

var loginfo = log.New(os.Stdout, "[info]:", log.LstdFlags)
var logerr = log.New(os.Stderr, "[err]:", log.LstdFlags)

func testTerminalSession() {
	t1_session.Main()
}

func test2_tcpnet() {
	// []byte{0, 0, 0, 0}, 1234},
	tcpAddr := net.TCPAddr{IP: []byte{0, 0, 0, 0}, Port: 8088}
	case1.ServerListener(&tcpAddr)
}

func GetTestReader() func() {
	// TODO 遇到了一个奇怪的问题, 同一段读取stdin的代码,在debug模式下无法阻塞的读取input流,run模式下正常.
	testreader := func() {
		for {
			reader := bufio.NewReader(os.Stdin)
			// ReadLine 是一个低级的原始的行读取操作
			// 大多数情况下，应该使用 ReadBytes('\n') 或 ReadString('\n')
			// 或者使用一个 Scanner
			//
			// ReadLine 通过调用 ReadSlice 方法实现，返回的也是缓存的切片
			// ReadLine 尝试返回一个单行数据，不包括行尾标记（\n 或 \r\n）
			// 如果在缓存中找不到行尾标记，则设置 isPrefix 为 true，表示查找未完成
			// 同时读出缓存中的数据并作为切片返回
			// 只有在当前缓存中找到行尾标记，才将 isPrefix 设置为 false，表示查找完成
			// 可以多次调用 ReadLine 来读出一行
			// 返回的数据在下一次读取操作之前是有效的
			// 如果 ReadLine 无法获取任何数据，则返回一个错误信息（通常是 io.EOF）
			line, isprefex, err := reader.ReadLine()
			loginfo.Printf("==>line:%v ,isprefix:%v, err:%v \n", line, isprefex, err)
		}
	}
	loginfo.Printf("==> %v \n", reflect.TypeOf(testreader))
	return testreader
}

func main() {
	test2_tcpnet()
	// testReader := case1_tcpnet.GetTestReader()
	// testReader := GetTestReader()
	
	// wait := make(chan int)
	// <-wait
	
}
