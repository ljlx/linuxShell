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
	// 2.字符串
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

/*
  一种类型的方法集是一个可以被该类型的值调用的所有方法的集合。如果该类型没有方法，则该集合为空。Go语言的interface{}类型用于表示空接口，即一个方法集为空集的类型的值。由于每一种类型都有一个方法集包含空的集合（无论它包含多少方法），一个interface{}的值可以用于表示任意Go类型的值。
 */
func case2_assert() {
	xint := int(123456)
	xfloat := float32(3.141592653)
	xfloat64 := float64(3.14159265300012389579823748)
	xint64 := int64(2423414352)
	xstr := "hello"
	
}

func Main() {
	case1_typeConv()
}
