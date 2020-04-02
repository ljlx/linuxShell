/*
--------------------------------------------------
 File Name: TestMain.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-13-上午10:35
---------------------说明--------------------------

---------------------------------------------------
*/

package main

import (
	"fmt"
)

type TestStructNil struct {
	i int
}

func (test TestStructNil) test() (int) {
	fmt.Println(test.i)
	fmt.Println(test)
	test.i += 1
	return test.i
}

func getTestStructNil() (*TestStructNil) {
	var tt *TestStructNil
	return tt
}

func main() {
	var i *int
	var tt TestStructNil
	// i = new(int)
	// 并不会引发类似java的nullpoint错误,原因是go初始化所有类型的时候,会给该类型赋值为对应的0值.结构体的0值就是该结构体内的所有类型皆是对应的0值.
	// bool 的0值就是flase.
	// 数值类型的0值就是0.
	// string ""
	// 指针的就是nil.
	tt2 := getTestStructNil()
	// 能判断一个对象是否为nil的说明该对象一定是指针.
	if tt2 != nil {
		fmt.Printf("tt is nil")
	}
	tt.test()
	//     就会报这样的一个错误
	//
	// panic: runtime error: invalid memory address or nil pointer dereference
	// [signal 0xc0000005 code=0x1 addr=0x0 pc=0x498025]
	//
	//    1
	//    2
	//
	//    报这个错的原因是 go 初始化指针的时候会为指针 i 的值赋为 nil ，但 i 的值代表的是 *i 的地址， nil 的话系统还并没有给 *i 分配地址，所以这时给 *i 赋值肯定会出错
	//    解决这个问题非常简单，在给指针赋值前可以先创建一块内存(调用new函数.)分配给赋值对象即可
	
	i = new(int)
	fmt.Println(i, &i, *i)
}
