/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: arraySlice.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-9-上午9:08
---------------------说明--------------------------
 4.2 数组和切片
---------------------------------------------------
*/

package arraySlice

import (
	"fmt"
	"reflect"
	"strings"
	
	"t1/p4_0_collect/point"
	"t1/p5_functionCode/p5_1_typeOper"
	
	"sort"
)

func case1_array() {
	fmt.Printf("\n----------------case1_array------------------\n")
	// 	数组使用以下语法创建：
	// [length]Type
	// [N]Type{value1, value2,..., valueN}
	// [...]Type{value1, value2,..., valueN}
	intarray := [10]int{}
	// 经过调试/xk发现这个字符串'数组',居然是一个切片.
	// 明白了.在声明的时候'[]'内定义了大小(或者...也行)的是数组,没定义大小的是切片
	strarray := [1]string{"123"}
	
	fmt.Printf("int数组:%v ,%v \n", intarray, reflect.TypeOf(intarray))
	fmt.Printf("str数组:%v ,%v \n", strarray, reflect.TypeOf(strarray))
	stutype := reflect.TypeOf(point.Student{})
	fmt.Printf("typeof %v \n", stutype)
	// 	如果在这种场景中使用了...（省略符）操作符，Go语言会为我们自动计算数	组的长度
	// 		在任何情况下，一个数组的长度都是固定的并且不可修改。
	// 	由于数组的长度是固定的，因此它们的容量总是等于其长度.
	// 对于数组而言cap()函数和len()函数返回的数字一样。
	// 数组可以使用与字符串或者切片一样的语法进行切片，只是其结果为一个切片，	而非数组。
	floatArray := [...]float32{3.13, 6.23409}
	fmt.Printf("自动计算长度的float数组:%v ,type:%v 	\n", floatArray, reflect.TypeOf(floatArray))
	intarray2 := [...][2]int{{1, 2}, {2, 2}, {3, 3}}
	fmt.Printf("自动计算长度的二维int数组:%v ,type: %T ,type2:%v , len: %2d \n", intarray2, intarray2, reflect.TypeOf(intarray2), len(intarray2))
	
	// 一般而言，Go语言的切片比数组更加灵活、强大且方便。数组是按值传递的（即传递副本，虽然可以通过传递指针来避免）而不管切片的长度和容量如何，传递成本都会比较小，因为它们是引用.
	// 	无论包含了多少个元素，一个切片在64位机器上是以16字节的值进行传递的，在32位机器上是以12字节的值进行传递的。）数组是定长的，而切片可以调整长度。
	// 数组和切片都可以使用表4-1中所给出的语法来进行切片。
	// 也就是说 go的数组也可以使用切片操作,并产生一个新的切片.切片语法是python的子集,不支持python的方向操作符
	fmt.Printf("\n----------------case1_array------------------\n")
}

// 切片测试
func case2_slice() {
	fmt.Printf("\n----------------case2_slice------------------\n")
	// 	Go语言中的切片是长度可变、容量固定的相同类型元素的序列。我们将在后文看到，虽然切片的容量固定，但也可以通过将其切片来收缩或者使用内置的append()函数来增长。多维切片可以自然地使用类型为切片的元素来创建，并且多维切片内部的切片长度也可变
	
	// 	由于go的类型可以是一个接口,因此可以保存任意满足所声明的接口的元素(即它们定义了该接口所需的方法),在这点上,我旭更喜欢java的语法,对接口实现强类型,实现接口的时候,必须和接口的名称绑定,这样好知道一个类型到底实现了哪些接口,也方便编译器帮助查找,一个接口有哪些类型实现并使用.
	// 一个空接口interface{} 可以表示是任意类型.在取出时需要(使用类型断言或者类型转变)
	//
	// 	可以使用如下语法来创建切片:
	// 	//使用make创建一个切片,实际上是创建一个隐藏的初始化为0的数组,然后返回一个引用该隐藏数组的切片.
	// 	//该隐藏的数组与 Go语言中的所有数组一样，都是固定长度的，如果使用第一种语法创建，那么其长度即为切片的容量.
	sliceInt := make([]int, 5, 10) // len:5,cap:10 第一种 len<=cap
	//
	// 其长度即为切片的长度
	// 第二种、第三种和第四种语法都是用于当我们希望其长度和容量相同时。
	sliceInt2 := make([]int, 4) // len:4,cap:4//第二种
	//
	var sliceInt3 []int
	sliceInt4 := []int{1, 1, 3, 5}
	// 语法[]Type{}与语法 make([]Type, 0)等价，两者都创建一个空切片
	// 我们可以使用内置的append()函数来有效地增加切片的容量
	fmt.Printf("第一种:%v ,len:%v ,cap:%v \n", sliceInt, len(sliceInt), cap(sliceInt))
	fmt.Printf("第二种:%v ,len:%v ,cap:%v \n", sliceInt2, len(sliceInt2), cap(sliceInt2))
	fmt.Printf("第三种:%v ,len:%v ,cap:%v \n", sliceInt3, len(sliceInt3), cap(sliceInt3))
	sliceInt4[3] += 1
	fmt.Printf("第四种:%v ,len:%v ,cap:%v \n", sliceInt4, len(sliceInt4), cap(sliceInt4))
	
	fmt.Printf("change slice. 验证切片是对同一个数组产生的引用.\n")
	//
	// 2. 验证切片与其隐藏数组的关系
	texthelloworld := "hello,go-world"
	
	originalSlice := strings.SplitAfter(texthelloworld, "")
	fmt.Printf("original slice: %v, now begin chanage.\n", originalSlice)
	slice_hello := originalSlice[:5]
	slice_comma := originalSlice[5:6]
	slice_comma[0] = "#"
	goworld := originalSlice[6:]
	goworld[2] = "#"
	fmt.Printf("original: %v \n helloSlice:%v \n goworld:%v \n", originalSlice, slice_hello, goworld)
	
	// 从以上这个例子可以看出,对切片出来的子切片做更改内容操作也会影响到上层切片, 所以他们所引用的是同一个切片对象.
	// 同一个底层数组的引用，其中一个改变会影响到其他所有指向该相同数组的任何其他引用
	//
	var originalEmptySlice []string // len:0,cap:0
	
	originalEmptySlice2 := new([10]string)[:] // len:10, cap:10
	// 使用内置的new()函数创建一个指向数组的指针，然后立即取得该数组的切片
	// 这会创建一个其长度和容量都与数组的长度相等的切片，但是所有元素都会被初始化为零值（在这里是空字符串）
	fmt.Printf("空切片:%v,%v \n", originalEmptySlice, originalEmptySlice2)
	originalEmptySlice2[0] = "he"
	originalEmptySlice2[5] = "llo"
	originalEmptySlice2[6], originalEmptySlice2[7] = ",", "world"
	originalEmptySlice2[9] = "."
	fmt.Printf("修改空切片里的值:%v", originalEmptySlice2)
	fmt.Printf("\n----------------case2_slice------------------\n")
	// 可以使用内置的append()函数来增加切片的容量.
	// append(sliceInt3,0,1,2)
}

func case2_slice_forRange() {
	intslice := []int{1, 2, 3, 4, 5, 6, 7, 8}
	sums := 0
	for _, item := range intslice {
		sums += item
	}
	top5_sums := 0
	// 切片循环前5个元素.如果想修改切片内值,就需要使用intslice[index]=值修改了,不能使用item副本方式修改.
	// TODO 这里range循环item是拷贝副本形式, 如果切片里的元素是大对象怎么办?
	fmt.Printf("准备在for...range中修改切片: %v \n", intslice)
	for index, item := range intslice[:5] {
		top5_sums += item
		intslice[index] += 10
	}
	fmt.Printf("修改后的切片: %v \n", intslice)
}

// ----------start----------结构体定义----------start----------
// 切片demo用student
type SliceStudent struct {
	// 姓名
	name string
	// 年龄
	age int
	// 身高
	height float32
	// 编号
	indexNums int
}

// func (student SliceStudent) String() string {
// 当需要传值的地方传入的是一个指针的时候，Go会自动将其解引用
// 但是最好还是在需要指针的时候,要声明需要的是一个指针,别依赖于语言的特性.容易出问题.
func (student *SliceStudent) String() string {
	// 	java.tostring()
	// (student SliceStudent) 相当于将这个函数绑定在这个结构体上,作为(java)方法.
	// 此处这个student值对象,相当于java的this,python的self
	strtext := ""
	//
	strbuilder := strings.Builder{}
	strbuilder.WriteString(fmt.Sprintf("name=%v ,", student.name))
	strbuilder.WriteString(fmt.Sprintf("age=%v ,", student.age))
	strbuilder.WriteString(fmt.Sprintf("height=%v ,", student.height))
	strbuilder.WriteString(fmt.Sprintf("indexNums=%v ", student.indexNums))
	//
	strtext = strbuilder.String()
	// student.name+="旭旭."
	student.height += 100
	return strtext
}

// ----------end------------结构体定义----------end------------

func case2_slice_struct() {
	hanxu := SliceStudent{}
	hanxu.name = "hanxu"
	hanxu.age = 22
	hanxu.height = 122
	hanxu.indexNums = 1
	fmt.Printf("%v \n", hanxu.String())
	fmt.Printf("%v \n", hanxu.String())
	//
	// 这里创建了一个包含指向SliceStudent指针(*SliceStudent)的切片([]*SliceStudent).
	// 然后立即使用了3个*SliceStudent(name= oldhanxu,jchen,qzpen) 来将其初始化
	// 相当于 这里是实现了 指针(*SliceStudent)的切片,之所以可以这样做是因为 Go语言足够灵活能够识别出来一个[]*SliceStudent需要的是指向SliceStudent的指针
	// stuslice:=[]SliceStudent{//
	stuslice := []*SliceStudent{ //
		{name: "oldhanxu", age: 33, height: 99, indexNums: 2}, //
		{name: "jchen", age: 22, height: 90, indexNums: 3},    //
		{name: "qzpen", age: 14, height: 100, indexNums: 4},   //
	}
	fmt.Printf("\n 2019年info:\n %v \n", stuslice)
	for _, item := range stuslice {
		// 在每一次遍历中，变量 item 被赋值为一个*SliceStudent副本，这是一个指向SliceStudent所对应的底层SliceStudent的指针
		item.age += 10
		// 	Q1: 这里用item.age 是否更改了stuslice列表对象里的元素,还是 item拷贝对象的一个值.
		// 结论:不可以更改,因为item是拷贝的副本对象.
		// 如果想要在for...range里修改item的值, 需要在创建stuslice时,使用指针的方式创建值,比如:
		// stuslice:=[]*SliceStudent{}
		
	}
	fmt.Printf("\n 2019年info(验证是否修改成功.):\n %v \n", stuslice)
	case2_slice_struct_change(stuslice)
	fmt.Printf("\n 2019年info(验证是否修改成功.):\n %v \n", stuslice)
}

// 创建指针切片的简化版,创建指针切片的多种方式.
func case2_slice_struct_simple() {
	// 1.
	stuslice := [10]*SliceStudent{
		{"testt", 11, 99, 1},
		{name: "test", age: 123, height: 333, indexNums: 2},
	}
	// 在4.1节中，我们使用&Type{}来创建一个该类型的新值，并立即得到了一个指向它的指针）
	fmt.Printf("方式一: %v", stuslice)
	// 2.
	stuslice[3] = &SliceStudent{"", 1, 2, 3}
	//
	// inttest:=[2]int{1,2}
	teststu := [1]SliceStudent{{"fff", 11, 22, 33}}
	fmt.Printf("%v", teststu)
	
}

// TODO 以我目前的认知, 这种方式暂时无法传递指针切片对象进去,后续在细细研究
// 除非外部创建这个切片的时候,就要指明是指针类型切片.
func case2_slice_struct_change(stuslice []*SliceStudent) {
	for _, item := range stuslice {
		item.name += ".point"
	}
}

// 内置的append()函数接受一个切片和一个或者更多个值，返回一个（可能为新的）切片，其中包含原始切片的内容并将给定的值作为其后续项。如果原始切片的容量足够容纳新的元素（即其长度加上新元素数量的和不超过切片的容量），append()函数将新的元素放入原始切片末尾的空位置，切片的长度随着元素的添加而增长。如果原始切片没有足够的容量，那么append()函数会隐式地创建一个新的切片，并将其原始切片的项复制进去，再在该切片的末尾加上新的项，然后将新的切片返回，因此需要将append()的返回值赋值给原始切片变量。
func case3_slice_append() {
	fmt.Printf("func case3_slice_append() start\n")
	s1 := []int{1, 2, 3, 4, 5}
	s2 := []int{55, 44, 33, 11, 22}
	s3 := make([]int, 1, 1)
	//
	s1 = append(s1, 6, 7, 8, 9) // append单独添加元素列表
	s2 = append(s2, 66, 77, 88, 99)
	s3 = append(s3, s1[:3]...) // append一个切片,需要在末尾添加...来保证切片的扁平化追加内部元素,而不是把一个切片当作一个元素追加.
	// 如果原始切片没有足够的容量，那么append()函数会隐式地创建一个新的切片，并将其原始切片的项复制进去，再在该切片的末尾加上新的项，然后将新的切片返回，因此需要将append()的返回值赋值给原始切片变量
	s3 = append(s3, s2[3:]...)
	fmt.Printf(" s1:%v,\n s2:%v, \n s3:%v\n", s1, s2, s3)
	fmt.Printf("func case3_slice_append() end\n")
	// TODO 	考虑到切片是将一个隐藏的数组的, 这里需要确定的是 通过append追加后,是以数组内容拷贝的形式追加进来的? 还是通过引用模式? 可以通过使用&取址符查看.
	
}

// 有时我们不仅想往切片的末尾插入项，也想往切片的前面或者中间插入项。
func case3_slice_appendEnd() {
	// 现在的需求是,需要在这个切片的前面插入abc,在该切片的末尾插入hijk, how?
	s := []string{"d", "e", "f"}
	s_insert := []string{"a", "b", "c"}
	s_middle0 := []string{"h", "i", "j", "k"}
	s_middle := []string{"l", "m", "n"}
	s_end := []string{"x", "y", "z"}
	// result:=s
	fmt.Printf("原始切片:%v \n", s)
	fmt.Printf("待插入orappend的切片: %v \n", s_insert)
	fmt.Printf("待插入orappend的切片: %v \n", s_middle0)
	fmt.Printf("待插入orappend的切片: %v \n", s_middle)
	fmt.Printf("待插入orappend的切片: %v \n", s_end)
	s = insertStringSliceCopy(s, s_insert, 0) // 在0的位置插入切片.
	fmt.Printf("1.改过后的切片:%v \n", s)
	s = insertStringSliceCopy(s, s_middle0, 6) // 在中间指定的位置插入切片.
	fmt.Printf("2.改过后的切片:%v \n", s)
	s = insertStringSliceCopy(s, s_middle, len(s)) // 在中间指定的位置插入切片.
	fmt.Printf("3.改过后的切片:%v \n", s)
	s = insertStringSliceCopy(s, s_end, len(s)) // 在末尾的位置插入切片.
	fmt.Printf("修改后最终结果:%v \n", s)
}

func insertStringSliceCopy(original []string, s_insert []string, index int) []string {
	// 以后数据的sum
	initlen := len(original) + len(s_insert)
	// 猜测未来可能需要考虑的扩容大小,比如java的list和map的扩容处理.
	// TODO float 涉及到四舍五入转型
	// initcap:=int(initlen*1.35)
	radiocap := 1                      // need >=1
	initcap := int(initlen * radiocap) // cap等于倍率的len大小
	newslice := make([]string, initlen, initcap)
	// 拷贝切片.返回实际拷贝的内容len,理论上是<=(len(original)+len(s_insert))
	// returns the number of elements copied
	// 待操作的数据项b:{4 5}
	// original:
	// 1 2 3  6 7 8 9
	// {  a  }{   c   }
	//
	// 在插入的位置,拷贝切片插入点之前的数据列表A
	atIndex := copy(newslice, original[:index])          // 将数据列表项a切割出来插入到newslice中.返回len(newslice)
	atIndex = copy(newslice[atIndex:], s_insert)         // 相当于是mm在newslice末尾进行append要插入的内容, 将要插入追加的内容b,拼到a的末尾.
	atIndex = copy(newslice[atIndex:], original[index:]) // 将c部拼在ab的末尾.
	//
	// copy(newslice, original[:index])          // 将数据列表项a切割出来插入到newslice中.返回len(newslice)
	// newslice = append(newslice, s_insert...)
	// newslice = append(newslice, original[index:]...)// 将原来被拆分的切片的尾端追加到末尾
	
	return newslice
}

// ----------start----------自定义排序类型----------start----------
type AliasSortString []string

// 取长度
func (slice AliasSortString) Len() int {
	return len(slice)
}

// 比较
func (slice AliasSortString) Less(i, j int) bool {
	strItem := slice[i]
	strItem = strings.ToLower(strItem)
	strItemNext := slice[j]
	strItemNext = strings.ToLower(strItemNext)
	// 通过自定义less方法来实现降序升序
	return strItem > strItemNext
}

// 交换
func (slice AliasSortString) Swap(i, j int) {
	slice[i], slice[j] = slice[j], slice[i]
}

// ----------end------------自定义排序类型----------end------------

func case4_slice_sort() {
	strslice := []string{"f", "w", "X", "A", "a", "b", "B", "j", "o", "a", "c"}
	intslice := []int{23, 5, 6, 126, 5, 3, 44, 32, 12, 7, 1, 0}
	original_intslice_issort := sort.IntsAreSorted(intslice)
	original_strslice_issort := sort.StringsAreSorted(strslice)
	if ! original_intslice_issort {
		fmt.Printf("int切片未排序,开始排序...%v \n", intslice)
		// 需要先排序好才行.
		// searindex := sort.SearchInts(intslice, 23) // 查找5 在未排序好的列表里的索引位置
		// fmt.Printf("查找,[%d]在切片[%v]中的索引位置:%v \n", 5, intslice, searindex)
		sort.Ints(intslice)
		original_intslice_issort = sort.IntsAreSorted(intslice)
	}
	if ! original_strslice_issort {
		fmt.Printf("str切片未排序,开始排序...%v \n", intslice)
		sort.Strings(strslice)
		// 字符串的排序完全是字节排序，这点我们在前面章节中已讨论过（参见3.2节）。这也意味着字符串的排序是区分大小写的
		original_strslice_issort = sort.StringsAreSorted(strslice)
	}
	fmt.Printf("排序后的切片:%v \n %v \n", strslice, intslice)
	// --------search------
	searindex := sort.SearchInts(intslice, 5) // 查找5 在排序好的列表里的索引位置
	fmt.Printf("查找,[%d]在切片[%v]中的索引位置:%v \n", 5, intslice, searindex)
	// -------custom sort---------
	
}

// ----------start----------search----------start----------
func case4_slice_search() {
	// 	sort.Sort()函数能够对任意类型进行排序，只要其类型提供了sort.Interface接口中定义的方法，即只要这些类型根据相应的签名实现了Len()、Less()和Swap()等方法。
	cusSortString := AliasSortString{"c", ",", "b", "a", "."}
	fmt.Printf("自定义排序string,原始数据:%v \n", cusSortString)
	sort.Sort(cusSortString)
	fmt.Printf("自定义排序string,排序后:%v \n", cusSortString)
	// 二分查找法,
	// Go提供了一个使用二分搜索算法的sort.Search()方法：每次只需比较log2n个元素（其中n为切片中的元素总数）。从这个角度看，一个含1 000 000个元素的切片线性搜索平均需要500 000次比较，最坏时需要1 000 000次比较。而二分搜索即便是在最坏的情况下最多也只需要20次比较
	testBinSearch := []int{5, 3, 2, 6, 73, 2, 34, 5, 232, 34, 63, 2, 154, 6}
	// 需要先排序下
	sort.Ints(testBinSearch)
	wantFind := 34
	fmt.Printf("排序后的int切片[%v],需要找[%d]的index,长度[%d]\n", testBinSearch, wantFind, len(testBinSearch))
	// sort.Search()函数接受两个参数：所处理的切片的长度和一个将目标元素与有序切片的元素相比较的函数，如果该有序切片是升序排序的则使用 >= 操作符，如果逆序排序则使用 <=操作符
	// 该函数必须是一个闭包，即它必须创建于该切片的作用域内。
	// 因为它必须将切片当成是其自身状态的一部分。
	searchResu := sort.Search(len(testBinSearch), func(i int) bool {
		fmt.Printf("查找过程:%d \n", i)
		return testBinSearch[i] >= wantFind
	})
	
	searchFunc := func(i int) bool {
		fmt.Printf("查找过程:%d \n", i)
		return testBinSearch[i] >= wantFind
	}
	searchResu = sort.Search(len(testBinSearch), searchFunc)
	// sort.Search()函数返回一个int型的值。只有当该值小于切片的长度并且在该索引位置的元素与目标元素相匹配时，我们才能够确定找到了需要找的元素
	if searchResu < len(testBinSearch) && testBinSearch[searchResu] == wantFind {
		// 不区分大小写的比较字符串.
		// strings.EqualFold("s","s")
		fmt.Printf("查找成功,二分查找法结果:%v\n", searchResu)
	} else {
		fmt.Printf("查找失败,二分查找法结果:%v\n", searchResu)
	}
	
}

// ----------end------------search----------end------------

func Main() {
	case1_array()
	case2_slice()
	case2_slice_forRange()
	case2_slice_struct()
	case3_slice_append()
	case3_slice_appendEnd()
	case4_slice_sort()
	case4_slice_search()
	// ospagesize:=os.Getpid()
	// syspagesize:=	syscall.Getpid()
	// fmt.Printf("%v,%v \n",ospagesize,syspagesize)
}
