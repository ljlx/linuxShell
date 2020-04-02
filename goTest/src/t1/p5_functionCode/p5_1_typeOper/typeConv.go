/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: p5_1_1_typeConv.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-14-下午1:01
---------------------说明--------------------------

---------------------------------------------------
*/

package p5_1_typeOper

import (
	"bytes"
	"fmt"
	"strings"
)

/*
Go语言提供了一种在不同但相互兼容的类型之间相互转换的方式，并且这种转换非常有用并且安全.
*/
func case1_typeConv() {
	// 类型转换语法
	// resultOfTargetType := TargetType(expression)
	
	// 1.对于数值类型之间的转换，可能会发生丢失精度或者其他问题.
	maxUint16 := uint16(65535)
	x := uint16(65500)     // 无符号16位2字节的,有效位是16位,有符号是15位,第一位是代表正负数的.
	y := int16(65535 >> 1) // 65535/2 == 65535>>1 => 32767
	// output: 转换前:x=65535,y=32767
	fmt.Printf("数字类型转换前:maxUint16=%d,x=%d,y=%d \n", maxUint16,
		x, y)
	// 尝试进行低位数字向高位数字转换. uint16(0~65535) >> int16(-32768~32767)
	// 由于uint16超出了int16的范围(32768~65535),因此会进行错误的转换(重置为0后继续递增.)
	y = int16(x)
	fmt.Printf("数字类型转换后:x=%d,y=%d \n", x, y)
	// 对于数字，本质上讲我们可以将任意的整型或者浮点型数据转换成别的整型或者浮点型（如果目标类型比源类型小，则可能丢失精度）
	// --------------------------------------------------
	// 2.字符串转换,与字节,码点的相互转换.
	// 一个字符串可以转换成一个[]byte（其底层为 UTF-8的字节）或者一个[]rune（它的Unicode码点），并且[]byte和[]rune都可以转换成一个字符串类型
	strtext := "hi,世界."
	byteText := []byte{104}
	runeText := []rune{'h'}
	fmt.Printf("字符转换前:strText=%v,byteText=%v,runeText=%v \n", strtext, byteText, runeText)
	str2byte := []byte(strtext)
	str2rune := []rune(strtext)
	byte2str := string(byteText)
	byte2rune := bytes.Runes(byteText)
	rune2str := string(runeText)
	// rune2byte := []byte(runeText)
	// byte数组和rune互相转换问题?, 应该是通过字符转换吧
	fmt.Printf("%v \n", strings.Repeat("-", 80))
	fmt.Printf("%-6s | string %-32s []rune \t []byte \n", "目标", "")
	// splieLine := fmt.Sprintf("%10s", "-")
	fmt.Printf("%v \n", strings.Repeat("-", 80))
	fmt.Printf("%s %5s %-37v  %v \t\t %v \n", "原文", "|", strtext, runeText, byteText)
	fmt.Printf("%s %2s %-37v  %v \t\t\t %v \n", "string", "|", strtext, rune2str, byte2str)
	fmt.Printf("[]rune \t %v \t\t\t %v \t\t %v \n", str2rune, runeText, byte2rune)
	fmt.Printf("[]byte \t %v %v \t\t %v \n", str2byte, runeText, "-")
	fmt.Printf("%v \n", strings.Repeat("-", 80))
}

type Student struct {
	/*
		mingzi,大些是对非同包名暴露
	 */
	Name  string
	Age   int
	Grade float32
}

func (stu Student) String() string {
	builder := strings.Builder{}
	builder.WriteString(fmt.Sprintf("Name=[%v],", stu.Name))
	builder.WriteString(fmt.Sprintf("Age=[%v],", stu.Age))
	builder.WriteString(fmt.Sprintf("chenji=[%v],", stu.Grade))
	return builder.String()
}

func (stu Student) myname() string {
	builder := strings.Builder{}
	builder.WriteString("myname:")
	builder.WriteString(stu.Name)
	return builder.String()
}

/*
  一种类型的方法集是一个可以被该类型的值调用的所有方法的集合。如果该类型没有方法，则该集合为空。Go语言的interface{}类型用于表示空接口，即一个方法集为空集的类型的值。由于每一种类型都有一个方法集包含空的集合（无论它包含多少方法），一个interface{}的值可以用于表示任意Go类型的值。
 */
func case2_assert() {
	// 感觉像java强制类型转换.
	// ----------start----------数据项定义----------start----------
	// stuhanxu := Student{"hanxu", 22}
	var xint interface{} = 99
	var a_stuUnknow interface{} = Student{"unknowhanxu", 33, 1.22}
	// ----------end------------数据项定义----------end------------
	// 类型断言
	// 在处理从外部源接收到的数据、想创建一个通用函数及在进行面向对象编程时，我们会需要使用interface{}类型（或自定义接口类型）。为了访问底层值，有一种方法是使用下面中提到的一种语法来进行类型断言：
	// resultOfType, boolean := expression.(Type) // 安全类型断言
	// resultOfType := expression.(Type) // 非安全类型断言，失败时panic()
	//
	// 成功的安全类型断言将返回目标类型的值和标识成功的true。如果安全类型断言失败（即表达式的类型与声明的类型不兼容），将返回目标类型的零值和false。非安全类型断言要么返回一个目标类型的值，要么调用内置的panic()函数抛出一个异常。如果异常没有被恢复，那么该函数会导致程序终止。（异常的抛出和恢复的内容将在后面阐述，参见5.5节。）
	a_stu_hanxu := a_stuUnknow.(Student)
	a_int := xint.(int)
	fmt.Printf("不安全断言(正确情况),结果:%v \t %v \n", a_int, a_stu_hanxu.myname())
	// ---------------------
	// panic: interface conversion: interface {} is p5_1_typeOper.Student, not int
	// TODO 如何捕获异常? 5.5节介绍
	// a_stu_hanxu_err := a_stuUnknow.(int)
	// a_int_err := xint.(float64)
	// fmt.Printf("不安全的断言(错误情况),error:%v ,%v", a_int_err, a_stu_hanxu_err)
	// ------------------------
	// 安全断言
	// TODO 影子变量问题?
	if a_stu_hanxu_err, ok := a_stuUnknow.(Student); ok {
		fmt.Printf("安全断言(正确情况),%v \n", a_stu_hanxu_err)
	}
	
	if a_stu_hanxu_err, ok := a_stuUnknow.(int); !ok {
		// 返回了对象结构体的0值
		fmt.Printf("安全情况(错误情况),that is not right type:%v \n", a_stu_hanxu_err)
	}
	
	if a_int_err, ok := xint.(Student); !ok {
		// 返回了对象结构体的0值
		fmt.Printf("安全断言(错误情况),that is not right type:%v \n", a_int_err)
	}
	// 做类型断言的时候将结果赋值给与原始变量同名的变量是很常见的事情，即使用影子变量。同时，只有在我们希望表达式是某种特定类型的值时才使用类型断言。（如果目标类型可以是许多类型之一，我们可以使用类型开关，参见5.2.2.2节。）
	
}

func Main() {
	case1_typeConv()
	case2_assert()
}
