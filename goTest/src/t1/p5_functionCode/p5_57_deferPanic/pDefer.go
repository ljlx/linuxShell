/*
--------------------------------------------------
 File Name: pDefer.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-21-下午5:55
---------------------说明--------------------------
 延迟函数测试
---------------------------------------------------
*/

package deferPanic

import (
	"fmt"
	"os"
)

/*
defer语句用于延迟一个函数或者方法（或者当前所创建的匿名函数）的执行，它会在外围函数或者方法返回之前但是其返回值（如果有的话）计算之后执行。这样就有可能在一个被延迟执行的函数内部修改函数的命名返回值（例如，使用赋值操作符给它们赋新值）。如果一个函数或者方法中有多个defer语句，它们会以LIFO（Last In Firs Out，后进先出）的顺序执行。
 */

func testFileDefer() {
	// defer语句最常用的用法是，保证使用完一个文件后将其成功关闭，或者将一个不再使用的通道关闭，或者捕获异常。
	
	fileinfo, error := os.Open("/tmp/ttt")
	defer func() {
		if error == nil {
			fmt.Printf("关闭文件流..\n")
			fileinfo.Close()
		} else {
			fmt.Printf("延迟执行函数,发现了错误,%v\n", error)
		}
	}()
	if error != nil {
		fmt.Fprintf(os.Stderr, "发生错误:%v\n", fmt.Errorf("文件无法读取,%v \n", error))
		return
	} else {
		filefd := fileinfo.Fd()
		fmt.Printf("filefd:%v", filefd)
	}
}

func close() {
	fmt.Printf("this is close.")
}

func testtt() {
	// 	这个模式在 Go语言中是一个标准做法[8]。虽然很少用到，我们当然也可以将该模式应用于自定义类型，为类型定义Close()或者Cleanup()方法，并将该方法用defer语法调用。
	fmt.Printf("进行资源的调用和相关操作")
	
	// 调用close接口的Close()函数
	defer close()
	
}

func Main_defer() {
	testFileDefer()
}
