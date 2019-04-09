package main

import "fmt"

func infiniteFor() {
	index := 1
	for {
		if index == 10 {
			break
		}
		index++
		fmt.Println(index)
	}
}

func forrange() {
	nums := []float64{1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9}
	sums := 0.0
	for _, item := range nums {
		//for...range循环首先初始化一个从0开始的循环计数器，在本例中我们使用空白符将该值丢弃（_），然后是从切片中复制对应元素。这种复制即使对于字符串来说也是代价很小的（因为它们按引用传递）。这意味着任何作用于该项的修改都只作用于该副本，而非切片中的项。
		sums += item
	}
	fmt.Printf("Σ%.1f -> %.1f \n", nums, sums)
}

func main() {
	infiniteFor()
	forrange()
}
