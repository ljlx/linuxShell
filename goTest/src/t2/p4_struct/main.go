package main

type struct_test struct {
	t1 int32
	t2 int32
	t3 string
	t4 bool
}

//空接口（没有定义方法的接口）用interfae{}来表示。[7]由于空接口没有做任何要求（因为它不需要任何方法），它可以用来表示任意值（效果上相当于一个指向任意类型值的指针），无论这个值是一个内置类型的值还是一个自定义类型的值
//顺便提一句，在Go语言中我们只讲类型和值，而非类和对象或者实例（因为Go语言没有类的概念）。
type Stack []interface{}

func t1(tess ...interface{}) {
	test := struct_test{1, 2, "3", true}
	println(test.t1 + test.t2)
	println(test.t3)
	println(test.t4)

}

func main() {
	t1(1, "sdf")
}
