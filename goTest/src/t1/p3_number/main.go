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
	"t1/p3_number/statistics"
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

/*
1706年，约翰·梅钦（John Machin）发明了一个计算任意精度 π 值的公式（见图2-1），我们可以将该公式与Go标准库中的big.Int结合起来计算 π，以得到任意位数的值。在图2-1中给出了该公式以及它依赖的arccot()函数。（理解这里介绍的big.Int包的使用无需理解梅钦的公式。）我们实现的arccot()函数接受一个额外的参数来限制计算结果的精度，以防止超出所需的小数位数。
 */
func testPI(places int) *big.Int {

	digits := big.NewInt(int64(places))

	unity := big.NewInt(0)

	ten := big.NewInt(10)

	exponent := big.NewInt(0)

	unity.Exp(ten, exponent.Add(digits, ten), nil)

	pi := big.NewInt(4)
	//TODO 没有这个函数arccot
	//left := arccot(big.NewInt(5), unity)
	//
	//left.Mul(left, big.NewInt(4))
	//
	//right := arccot(big.NewInt(239), unity)
	//
	//left.Sub(left, right)
	//
	//pi.Mul(pi, left)
	return pi.Div(pi, big.NewInt(0).Exp(ten, ten, nil))
	//return nil
}

func test1() {
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

func testStatistics() {
	statistics.DoStatisTest()
}

func main() {
	testStatistics()
}

/*
Go语言也像C和Java一样不支持操作符重载，提供给big.Int和big.Rat类型的方法有它自己的名字，如Add()和Mul()。
在大多数情况下，方法会修改它们的接收器（即调用它们的大整数），同时会返回该接收器来支持链式操作
 */
func testBigIntNumber() {

	var defint int64 = 111111111111116
	bigintt := big.NewInt(defint)
	var defint2 = big.NewInt(defint - 2)
	var defint3 = big.NewInt(defint - 3)

	fmt.Printf("原始值: bigintt[%d] ,defint2[%d] ,defint3[%d] \n",bigintt,defint2,defint3)


	bigint_result_sub := bigintt.Sub(defint2, defint3)
	bigint_result_add := bigintt.Add(defint2, defint3)
	fmt.Printf("big number: [%d]+[%d]=[%d] \n", defint2, defint3, bigint_result_add)
	fmt.Printf("big number: [%d]-[%d]=[%d] \n", defint2, defint3, bigint_result_sub)
	fmt.Printf("计算后值: bigintt[%d] ,defint2[%d] ,defint3[%d] \n",bigintt,defint2,defint3)
	//### 问题1. >>  bigintt bigint_result_sub bigint_result_add的最终计算结果值是一样的,
	//是因为每次返回的计算结果是bigintt值的一个指针引用.相当于返回bigintt自身(return this)
	//作用是因为,计算结果方便用来链式计算处理.

}

/*
使用Go语言内置的float64类型，我们可以很精确地计算包含大约15位小数的情况，这在大多数情况下足够了。
但是，如果我们想要计算包含更多位小数，即数十个甚至上百个小数时，例如计算 π的时候，
那么就没有内置的类型可以满足了。
 */
func testbigFloat()  {

}

