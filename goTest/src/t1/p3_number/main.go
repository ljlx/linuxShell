/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: main.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-3-29-下午4:03
---------------------说明--------------------------
 数字类型学习.
---------------------------------------------------
*/

package main

import (
	"math/big"
	"fmt"
	"math"
)

type bigint big.Int

type hxint32 int32

type hxint int

//每一个数值类型都不同，这意味着我们不能在不同的类型（例如，类型int32和类型int）之间进行二进制数值运算或者比较操作（如+或者＜）

func bigNum() {
	//ii := bigint(12)
	//println(ii)
}

//为了执行缩小尺寸的类型转换，我们可以创建合适的函数。例如：

func testt() {
	const factor = 3 // factor与任何数值类型兼容
	i := 20000       // 通过推断得出i的类型为int
	i *= factor
	j := int16(20)       // j的类型为int16，与这样定义效果一样：var j int16 = 20
	i += int(j)          // 类型必须匹配，因此需要转换
	k := uint8(0)        // 效果与这样定义一样：var k uint8
	k = uint8(i)         // 转换成功，但是k的值被截为8位
	fmt.Println(i, j, k) // 打印：60020 20 16
}

func Uint8FromInt(x int) (uint8, error) {

	//当然，无符号的类型没有最小值常量，因为它们的最小值都为 0。
	if 0 <= x && x <= math.MaxUint8 {

		return uint8(x), nil

	}

	return 0, fmt.Errorf("%d is out of the uint8 range", x)

}

func main() {
	var i = 800
	var j int64 = 3

	//无类型的数值常量可以兼容表达式中任何（内置的）类型的数值，因此我们可以直接将一个无类型的数值常量与另一个数值做加法，或者将一个无类型的常量与另一个数值进行比较，无论另一个数值是什么类型（但必须为内置类型）
	ii := 1234
	jj := 56789
	//invalid operation: i + j (mismatched types int and int32)
	//不同类型的数值类型无法运算.
	//每一个数值类型都不同，这意味着我们不能在不同的类型（例如，类型int32和类型int）之间进行二进制数值运算或者比较操作（如+或者＜）
	//解决办法:
	//如果我们需要在不同的数值类型之间进行数值运算或者比较操作，就必须进行类型转换，通常是将类型转换成最大的类型以防止精度丢失。类型转换采用 type(value)的形式，只要合法，就总能转换成功——即使会导致数据丢失。
	//fmt.Printf("%s", reflect.Type(i).String())
	//ijsum := reflect.Type(i)

	fmt.Printf("有类型运算: int[%d], int32[%d], err-sum[%d], sum[%d] ,mochu[%d] \n", i, j, int8(i)+int8(j), int(i)+int(j), int(i)%int(j))
	fmt.Printf("无类型数值运算: [%d], [%d] , sum[%d] \n", ii, jj, ii+jj)
}
