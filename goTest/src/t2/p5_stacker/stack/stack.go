package stack

//.Go语言的空接口扮演的是Java中的Object或者C/C++中的void*类型一样的角色。
type Stack []interface{}

/**
	sstack 称为接收器.接收器是按值传递的
 */
func (sstack Stack) Len() int {
	//这也意味着任何对该接收器的改变都只是作用于其原始值的一份副本，因此会丢失。
	// 这对于不需要修改接收器的方法来说是没问题的
	//这个方法里改变接收器值是无意义的,因为改变的只是这个方法栈内的拷贝变量.

	return len(sstack)
}

/**
	容量大小.
 */
func (stack Stack) Cap() int {
	return cap(stack)
}
/**
	如果我们要修改接收器，就必须将接收器设为一个指针
Go语言中的指针除了不支持指针运算之外（其实也不需要），其他的与C和C++里的是一样的。
 */
func (sstack *Stack) Push(item interface{}) {
	//内置的append()函数可以将一个或多个值追加到一个切片里去，并返回一个切片（可能是新建的）
	// ，该切片包含原始切片的内容和在尾部追加进去的内容。
	nowstack := append(*sstack, item)
	*sstack = nowstack
}
/**
	在其他语言中，接收器一般被称为(java)this或(python)self，使用这种称谓在Go语言中也没问题，但被认为是不太好的Go语言风格。
 */
func (sstack Stack) Pop() interface{} {
	return len(sstack)
}

func asdf(ss string) {

}
