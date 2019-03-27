package stack

import "errors"

//由于Go语言的所有类型都实现了空接口，因此任意类型的值都可以存储在Stack中。
//.Go语言的空接口扮演的是Java中的Object或者C/C++中的void*类型一样的角色。
type Stack []interface {
}

/**
	sstack 称为接收器.接收器是按值传递的
 */
func (sstack Stack) Len() int {
	//这也意味着任何对该接收器的改变都只是作用于其原始值的一份副本，因此会丢失。
	// 这对于不需要修改接收器的方法来说是没问题的
	//这个方法里改变接收器值是无意义的,因为改变的只是这个方法栈内的拷贝变量.

	return len(sstack)
}

//通常所有的自定义数据集合类型（包括我们自己实现的以及Go语言标准库中的自定义数据集合类型）都应实现Len()和Cap()方法。
/**
	容量大小.
 */
func (stack Stack) Cap() int {
	return cap(stack)
}

/**
	如果我们要修改接收器，就必须将接收器设为一个指针
Go语言中的指针除了不支持指针运算之外（其实也不需要），其他的与C和C++里的是一样的。
hx940929-Note: 因为默认接收器函数是按值传递,那么如果不用指针,就会将原来的值(对象)拷贝一份到这个函数体内进行. 这里有两个需要注意的问题:
	1.对该值的任何修改,只是在函数内的副本进行,不会影响到函数的调用者所使用的值(对象)
	2.如果该值是一个大对象,那么在进行内存拷贝的时候,浪费性能和内存空间.效率低.
使用指针,就不会出现内存拷贝的问题,但是会有一个问题,就是允许函数内对值的任意修改.
 */
func (sstack *Stack) Push(item ...interface{}) {
	//内置的append()函数可以将一个或多个值追加到一个切片里去，并返回一个切片（可能是新建的）
	// ，该切片包含原始切片的内容和在尾部追加进去的内容。
	nowstack := append(*sstack, item)
	//我们可以通过解引用操作来获取该指针所指向值的实际Stack值，解引用操作只是简单意味着我们在试图获得该指针所指处的值。解引用操作通过在变量前面加上一个星号来完成,因此，我们写stack时，是指一个指向Stack的指针（也就//是一个 *Stack）。写*stack时，是指解引用该指针变量，也就是引用该指针所指之处的实际Stack类型值。
	//TODO 可以验证一下,如果不使用解引用操作, 直接操作指针对象会发生什么.
	*sstack = nowstack
}

/**
	在其他语言中，接收器一般被称为(java)this或(python)self，使用这种称谓在Go语言中也没问题，但被认为是不太好的Go语言风格。
 */
func (sstack Stack) Pop() (interface{}, error) {
	return nil, nil
}

func (sstack Stack) Top() (interface{}, error) {
	currLen := len(sstack)
	index := 0
	if currLen > 0 {
		index = currLen - 1
		item := sstack[index]
		//TODO 删除队列里的元素.
		return item, nil
	}
	return nil, errors.New("this stack is empty.")
}

func asdf(ss string) {

}

//TODO 需要了解下,GO中引用和切片的区别.
//需要注意的是，Go语言中的通道（channel）、映射（map）和切片（slice）等数据结构必须通过make()函数创建，而且make()函数返回的是该类型的一个引用。引用的行为和指针非常类似，当把它们传入函数的时候，函数内对该引用所做的任何改变都会作用到该引用所指向的原始数据。然而，引用不需要被解引用，因此大部分情况下不需要将其与星号一起使用。但是，如果我们要在一个函数或者方法内部使用 append()修改一个切片（不同于仅仅修改其中的一个元素内容），必须要么传入指向这个切片的一个指针，要么就返回该切片（也就是将原始切片设置为该函数或者方法返回的值），因为有时候append()返回的切片引用与之前所传入的不同。