/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: point.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-8-上午11:01
---------------------说明--------------------------
 指针学习练习
---------------------------------------------------
*/

package point

import (
	"fmt"
	"image/color"
)

//在某些场景下，我们需要传递非引用类型的可修改值，或者需要高效地传入大类型的值，这个时候我们需要用到指针。Go语言提供了两种创建变量的语法，同时获得指向它们的指针。
// 1.其中一种方法是使用内置的new()函数，
// 2. 另一种方法是使用地址操作符。
// 为了比较一下，我们将介绍这两种语法，并用两种语法分别创建一个扁平结构的结构体类型值。

type Student struct {
	name      string
	age       int
	lovething []string
}
type point struct {
	x, y int
}

//带有颜色,位置信息的矩形
type rectangle struct {
	positionA point
	positionB point
	positionC point
	positionD point
	fillcolor color.RGBA
}

func TestCase1() {
	//我们可以创建 composer 值或指向 composer 值的指针,，即*composer类型的变量
	stu_hanxu := Student{"oldhanxu", 25, nil} //创建一个名为试图_hanxu变量,其为Studeng类型的值
	stu_hanxu.age *= 1
	fmt.Printf("%v \n", stu_hanxu)
	// ----------start--------------------start----------
	//当 Go语言打印指向结构体的指针时，它会打印解引用后的结构体内容，但会将取址操作符&作为前缀来表示它是一个指针
	//new(Type) ≡&Type{} //使用new函数等同于大括号初始化法 结构体.
	//这两种语法都分配了一个Type类型的空值，同时返回一个指向该值的指针。如果Type不是一个可以使用大括号初始化的类型，我们只可以使用内置的new()函数
	//大括号初始化法只适用于结构体.
	//1. 使用new()函数来创建一个结构体
	stu_point_hanxu := new(Student)
	stu_point_hanxu.age = 23
	stu_point_hanxu.name = "newhanxu"
	fmt.Printf("%v \n", stu_point_hanxu)
	//2.
	stu_empty_jchen := &Student{} //指向student的指针
	stu_empty_jchen.name, stu_empty_jchen.age = "chenjian", 22
	fmt.Printf("%v \n", stu_empty_jchen)
	//3.
	stu_point_qzp := &Student{"quzhipen", 14, nil}
	stu_point_qzp.age += 1
	fmt.Printf("%v \n", stu_point_qzp)
	// ----------end----------------------end------------

}

//slice切片的定义和使用
func case2() {
	fmt.Println("case2>>>>>>>>>>>>>>>>>>>>>>>")
	grades := []int{11, 22, 33, 44, 55, 66, 77, 88, 99, 100}

	case2_inflate(grades, 3)

	lovething := []string{"code", "game", "ebook", "tv", "buy"}
	hanxuStu := &Student{"hanxu", 22, lovething}
	hanxuStu.age *= 1

}

//这里传入的是一个切片,并不是一个数组
//这里我们在一个整型切片之上进行一个操作。映射和切片都是引用类型，并且映射或者切片项中的任何修改（无论是直接的还是在它们所传入的函数中间接的修改）对于引用它们的变量来说都是可见的。
//TODO 所以这个函数里对grades的任何修改,都会作用于函数调用者,所传的值.相当于这个grades是一个指针, 但实际他是个切片, so 切片和数组的区别是?
func case2_inflate(grades []int, i int) {
	//我们没有使用for index、item...range这样的循环是因为这样只能得到其所操作的切片元素的副本，导致其副本与因数相乘之后将该值丢弃，而原始切片的值则保持不变
	//相当于这里的每一个item都是grades切片中的元素拷贝.浪费性能和内存空间
	//应该直接使用grades[index]来获取和更改切片元素的值,效率高.
	for index, item := range grades {
		grades[index] *= i
		fmt.Printf("index:[%d], item:[%d] \n", index, item)
	}
	fmt.Printf("修改后的成绩,%v \n", grades)
}

//矩形例子
func case3() {
	//	现在我们可以创建一个矩形类型的值，打印它的内容，调整大小，然后再打印它的内容。
	A := point{1, 2}
	B := point{2, 2}
	C := point{1, 1}
	D := point{2, 1}
	//黑色的矩形
	blackRect := &rectangle{A, B, C, D, color.RGBA{255, 255, 255, 10}}
	//向左移动2,向上移动3
	fmt.Printf("矩形向量信息(原始) \t %v \n", blackRect)
	case3_resizeRect(blackRect, 2, 3)
	fmt.Printf("矩形向量信息(change):\t %v \n", blackRect)
	case3_resizeRect(blackRect, -2, -3)
	fmt.Printf("矩形向量信息(回到原点):\t %v \n", blackRect)
	case3_resizeRect(blackRect, -1, -1)
	fmt.Printf("矩形向量信息(change):\t %v \n", blackRect)
}

//随机改变下位置,(x,y)可能为负数,代表其运动的方向.
//比如向x轴-正方向轴移动 2个单元格,就把所有的x+2
func case3_resizeRect(rectInstance *rectangle, x, y int) *rectangle {
	//if rectInstance != nil{
	//TODO 罗嗦的编码方式,怎么优化?
	//＂.＂操作符能够自动解引用结构体 ,所以里面的point值对象,不需要显示的&取值操作了.
	rectInstance.positionA.x += x
	rectInstance.positionB.x += x
	rectInstance.positionC.x += x
	rectInstance.positionD.x += x
	//y
	rectInstance.positionA.y += y
	rectInstance.positionB.y += y
	rectInstance.positionC.y += y
	rectInstance.positionD.y += y

	return rectInstance
}

func case4() {
	fmt.Println("func case4() {")
	a := 10
	point_b := &a
	point_b1 := &a
	*point_b += 1
	case4_a(&a)
	case4_a(point_b)
	fmt.Printf("%v,%v,%v,%v", a, point_b, &point_b, &point_b1)
}
func case4_a(intpoint *int) {
	*intpoint = *intpoint + 1
}

func TestMain() {
	TestCase1()
	case2()
	case3()
	case4()
}
