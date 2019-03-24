package main

import (
	test "fmt"
	. "time"

	"os"
)

func main() {
	test.Print("test")
	println("start...")
	//time.Now()
	println("",Now().String())
	println(os.Args[1])
}
