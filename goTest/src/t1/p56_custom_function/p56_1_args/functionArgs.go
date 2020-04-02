/*
--------------------------------------------------
 File Name: functionArgs.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-21-下午11:52
---------------------说明--------------------------
 函数参数相关练习学习.
---------------------------------------------------
*/

package functionArgs

import (
	"fmt"
	"math"
)

// 将函数调用作为函数的参数
// 如果我们有一个函数或者方法，接收一个或者多个参数，我们可以理所当然地直接调用它并给它相应的参数。另外，我们可以将其他函数或者方法调用作为一个函数的参数，只要该作为参数的函数或者方法的返回值个数和类型与调用函数的参数列表匹配即可。

// TODO 这里的一个问题是, 如果我函数的接受参数和类型于另一个函数的返回参数类型不一致,而我又想使用函数传参数,怎么办?
// 比如a(int,bool) b(int)(int,err) 我想将b函数的返回结果(int,err)给a,但是忽略错误err.

// TODO 海伦三角形公式很神奇啊.
/*
 一个函数要求传入三角形的边长（以 3 个整型数的方式），然后使用海伦公式计算出三角形的面积
 */
func getArea() {
	for i := 1; i <= 4; i++ {
		a, b, c := pythagoreanTriple(i, i+1)
		{
			triangle_1 := heron(a, b, c)
			triangle_2 := heron(pythagoreanTriple(i, i+1))
			fmt.Printf("∆1 == %10f == ∆2 == %10f\n", triangle_1, triangle_2)
		}
	}
}

/*
使用海伦三角公司根据边长求面积.

 */
func heron(a, b, c int) float64 {
	α, β, γ := float64(a), float64(b), float64(c)
	s := (α + β + γ) / 2
	return math.Sqrt(s * (s - α) * (s - β) * (s - γ))
}

/*
使用勾股定理生成一些三角形边长.
该函数使用了命名返回值（算是对该函数文档的一些补充）
 */
func pythagoreanTriple(m, n int) (a, b, c int) {
	if m < n {
		m, n = n, m
	}
	return (m * m) - (n * n), (2 * m * n), (m * m) + (n * n)
}

// ----------start----------可变长参数----------start----------
func changeLenghArgs(first int, nums ...int) {

}

// ----------end------------可变长参数----------end------------

func Main() {
	// 5.6.1.1 将函数调用作为函数的参数
	getArea() // B函数返回参数,作为A函数的入参.
	//
	// 5.6.1.2 可变参数函数,和java那个可变长参数是一样的.
	// 所谓可变参数函数就是指函数的最后一个参数可以接受任意个参数。这类函数在最后一个参数的类型前面添加有一个省略号。在函数里面这个参数实质上变成了一个对应参数类型的切片。例如，我们有一个签名是Join(xs...string)的函数，xs的类型其实是[]string。
}
