package mytest

import (
	test "fmt"
	. "time"

	"os"
	"reflect"
)

//GCtype=uint8
var inta = 10
var intb int8 = 10
var uintb uint8 = 10
var intc int16 = 10
var intd int64 = 10
var uintc uint16 = 10
var uintd uint64 = 10

func main() {
	println("数据类型学习start...")
	var int_inta = reflect.TypeOf(inta)
	println("int_inta : ",int_inta )
	var int8_intb = reflect.TypeOf(intb)
	println("int8_intb : ",int8_intb )
	var uint8_uintb = reflect.TypeOf(uintb)
	println("uint8_uintb : ",uint8_uintb )
	var int16_intc = reflect.TypeOf(intc)
	println("int16_intc : ",int16_intc )
	var int64_intd = reflect.TypeOf(intd)
	println("int64_intd : ",int64_intd )
	var uint16_uintc = reflect.TypeOf(uintc)
	println("uint16_uintc : ",uint16_uintc )



	println("数据类型学习end...")

	test.Print("test")
	println("start...")
	//time.Now()
	println("", Now().String())
	println(os.Args[0])
}
