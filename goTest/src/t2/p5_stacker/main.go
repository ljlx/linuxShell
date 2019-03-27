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
		if toperr == nil {
			fmt.Printf("curr top is :", topitem)
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
