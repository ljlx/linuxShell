/**
 * 功能说明:
 * 一些说明写这里
 * @author hanxu
 * @CreateDate 2019-03-29 下午2:05
 * @webSite https://www.thesunboy.com
 * @github https://github.com/thesunboy-com
*/
package main

import (
	"fmt"
	"strings"
	"math"
)

// ----------start----------第一种常量----------start----------
const test1_1 = 0
const test1_2 = 0

// ----------end------------第一种常量----------end------------

// ----------start----------第二种----------start----------
const (
	test2_1 = 0
	test2_2 = 1
	test2_3
	test2_4
)

//未指定值的时候,会使用上一个常量的值,作为下一个常量值
// ----------end------------第二种----------end------------

// ----------start----------第三种----------start----------
const (
	test3_0 = iota
	test3_1
	test3_2
	test3_3
	test3_4
)

//使用iota时,从0开始自增1
// ----------end------------第三种----------end------------

//==============iota==============
//也可以将iota与浮点数、表达式以及自定义类型一起使用。
type BigFlag int

/*
	Go语言很容易控制自定义类型的值如何打印，因为如果某个类型定义了String()方法，那么fmt包中的打印函数就会使用它来进行打印。因此，为了让 BitFlag 类型可以打印出更多的信息，我们可以给该类型添加一个简单的String()方法
 */
func (flag BigFlag) String() string {
	println("BigFlag..tostring", flag)
	var flags []string
	if flag&Active == Active {
		flags = append(flags, "Active")
	}
	if flag&Send == Send {
		flags = append(flags, "Send")
	}
	if flag&Receive == Receive {
		flags = append(flags, "Receive")
	}
	if len(flags) > 0 { // 在这里，int(flag)用于防止无限循环，至关重要！
		strresult := fmt.Sprintf("%d(%s)", int(flag), strings.Join(flags, "|"))
		return strresult
	}

	return "0()"
}

const (
	//常量值使用BigFlag类型, 默认为1左移0位,最终值为1
	Active  BigFlag = 1 << iota
	Send     //隐式地设置成BitFlag = 1 << iota　// 1 << 1 == 2
	Receive  //隐式地设置成BitFlag = 1 << iota　 // 1 << 2 == 4
)

func test1() {
	//我们可以略去自定义类型，这样Go语言就会认为定义的常量是无类型整数，并将 flag的类型推断成整型
	flag := Active | Send | Receive

	// ----------start----------问题----------start----------
	//BitFlag 类型的变量可以保存任何整型值，然而由于BitFlag是一个不同的类型，因此只有将其转换成int型后才能将其与int型数据一起操作（或者将int型数据转换成BitFlag类型数据）
	//不对啊 ,明明可以和int进行计算
	jttt := Active + 2
	println(jttt)
	println(BigFlag(3))
	// ----------end------------问题----------end------------

	//TODO 或运算 怎么计算的? 使用场景?
	flag1 := 2 | 2
	//println(fmg)("flag ==> %s, %d", flag,flag1)
	fmt.Printf("flag info==> %s, %s \n", flag, flag1)
	fmt.Printf("flag value==> %d, %d \n", flag, flag1)
	fmt.Printf("flag bin-value==> %b, %b ,%b \n", flag, flag1, 'A')

}

//常量表达式的值在编译时计算，它们可能使用任何算术、布尔以及比较操作符
const (
	MaxInt8   = 1<<7 - 1
	MinInt8   = -1 << 7
	MaxInt16  = 1<<15 - 1
	MinInt16  = -1 << 15
	MaxInt32  = 1<<31 - 1
	MinInt32  = -1 << 31
	MaxInt64  = 1<<63 - 1
	MinInt64  = -1 << 63
	MaxUint8  = 1<<8 - 1
	MaxUint16 = 1<<16 - 1
	MaxUint32 = 1<<32 - 1
	MaxUint64 = 1<<64 - 1

	// /*
	//   math包：
	//    */
	//   i := -100
	//   fmt.Println(math.Abs(float64(i))) //绝对值
	//   fmt.Println(math.Ceil(5.0)) //向上取整
	//   fmt.Println(math.Floor(5.8)) //向下取整
	//   fmt.Println(math.Mod(11, 3)) //取余数，同11%3
	//   fmt.Println(math.Modf(5.26)) //取整数，取小数
	//   fmt.Println(math.Pow(3, 2)) //x的y次方
	//   fmt.Println(math.Pow10(4)) // 10的n次方
	//   fmt.Println(math.Sqrt(8)) //开平方
	//   fmt.Println(math.Cbrt(8)) //开立方
	//   fmt.Println(math.Pi)

)

func main() {
	area_circle := math.Pi * math.Pow(2, 2)
	//TODO 查看值的类型,如何答应出type方法的值

	println("计算圆的面积: ", area_circle)
	println("start...")
	test1()
}
