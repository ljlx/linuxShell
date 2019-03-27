package main

import (
	"t2/p5_stacker/stack"
	"fmt"
)

func main() {


	var haystack stack.Stack

	haystack.Push("hay")

	haystack.Push(-15)

	haystack.Push([]string{"pin", "clip", "needle"})
	haystack.Push(12, 123, 123)
	haystack.Push(81.52)

	for {
		topitem, toperr := haystack.Top()
		//Go语言使用nil来表示空指针（以及空引用）
		//即表示指向为空的指针或者引用值为空的引用。[10]这种指针只在条件判断或者赋值的时候用到，而不应该调用nil值的成员方法
		if toperr == nil {
			fmt.Println("curr top is :", topitem)
		}

		item, err := haystack.Pop()

		if err != nil {
			break
		}
		if item == nil {
			return
		}

		fmt.Println(item)

	}
}

//Go语言中的构造函数从来不会被显式调用。相反地，Go语言会保证当一个值创建时，它会被初始化成相应的空值。例如，数字默认被初始化成0，字符串默认被初始化成空字符串，指针默认被初始化成nil值，而结构体中的各个字段也被初始化成相应的空值。因此，在Go语言中不存在未初始化的数据，这减少了很多在其他语言中导致出错的麻烦。