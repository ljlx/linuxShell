package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	//hello()
	goget()

}

func hello() {
	who := "world"
	if len(os.Args) > 1 {
		who = strings.Join(os.Args[0:], " ")
	}
	fmt.Println("hello, ", who)
}


func goget() {
	for i:=1;i<=3;i++ {
		if i>=2 {
			fmt.Print("当前的i值为：")
			fmt.Print(i)
			fmt.Print("\n")
			continue
		}
		fmt.Print("慕课网\n")
	}

}