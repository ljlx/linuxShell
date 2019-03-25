
package main

import (
	"os"
	"strings"
	"fmt"
)

//第一种
//import (
//	"fmt"
//	"os"
//	"strings"
//)
//多行导入
//import "os"
//import "strings"
//import "fmt"

//import导入规则.



// 定义常量 const name type = value
const usernameLen = 5
const username = "hanxu"
// 也会自动根据后面的值类型确定
const usernameLen1 = 5
//定义变量,在函数外定义的变量就是全局变量.
var appname = "hello.go"


// 定义一个名字叫hanxuInt的类型,它的类型是int,相当于其他语言中的类型别名
// TODO 不明白它的作用.
type hanxuInt int

//结构体声明
type user struct{

}

//声明接口,应该是面向对象里的接口
type IUser interface {

}

//启动点,相当于java的规则,不同的是,main函数必须处于main package下才行.
func main() {
	hello()
	goget()
	//masin()
	print( 	"warn:", usernameLen)
	println("warnln", appname)
}

//定义函数
func hello() {
	var who = "world"
	who1 := "secendwho"
	println(who1)
	if len(os.Args) > 1 {
		//切片语法和python相近.

		who = strings.Join(os.Args[1:4], ",")
		who1 = who
	}
	fmt.Println("hello, ", who)
}

func goget() {
	for i := 1; i <= 3; i++ {
		if i >= 2 {
			fmt.Print("当前的i值为：")
			fmt.Print(i)
			fmt.Print("\n")
			continue
		}
		fmt.Print("testttt\n")
	}

}
