/*
--------------------------------------------------
 File Name: switchAndIf.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-14-下午5:39
---------------------说明--------------------------
 分支: switch 和 if的学习
---------------------------------------------------
*/

package p5_2_switch

import (
	"fmt"
	
	"t1/p5_functionCode/p5_1_typeOper"
)

/*
	普通switch,表达式switch
 */
func case1_expression() {
	// /Go语言的switch语句不会自动地向下贯穿（因此不必在每一个case子句的末尾都添加一个break语句）。相反，我们可以在需要的时候通过显式地调用fallthrough语句来这样做。
	// 	switch optionalStatement; optionalExpression {
	// case expressionList1: block1
	// …
	// case expressionListN: blockN
	// default: blockD
	// }
	
	testtext := "test"
	testint2 := 10
	
	switch testtext {
	case "testtt":
		fmt.Println("this is %s", testtext)
	case "test":
		fmt.Printf("yes this is ok : %v \n", testtext)
	
	case "www":
		fmt.Println("not fallthrough")
		fallthrough
	case "lalalal":
		fmt.Println("hahahaha")
	default:
		fmt.Println("lalalla i am default.")
	}
	
	switch lala := testint2 - 5; lala {
	case 1:
		fmt.Println("nonono")
	case 5:
		fmt.Println("yes ok: ", lala)
	case 8, 9, 10:
		fmt.Println("error ")
	}
	
}

/*
注意，我们之前提到过类型断言（参见5.1.2节），当我们使用interface{}类型的变量时，我们常常需要访问其底层值。如果我们知道其类型，就可以使用类型断言，但如果其类型可能是许多可能类型中的一种，那我们就可以使用类型开关语句。
 */
func case2_type(items ...interface{}) {
	// 感觉可以用java实现,switch testClass.class { case String.class: sout(输出) break; }
	// Go语言的类型开关语法如下：
	// switch optionalStatement; typeSwitchGuard {
	// case typeLis1: block1
	// ...
	// case typeListN: blockN
	// default: blockD
	// }
	
	for i, x := range items {
		// xtype := x.(type)
		// Use of .(type) outside type switch
		// fmt.Printf("i:%v ,type: %v \n", i, x)
		switch x.(type) {
		case bool:
			fmt.Printf("param #%d is a bool\n", i)
		case float64:
			fmt.Printf("param #%d is a float64\n", i)
		case int, int8, int16, int32, int64:
			fmt.Printf("param #%d is an int\n", i)
		case uint, uint8, uint16, uint32, uint64:
			fmt.Printf("param #%d is an unsigned int\n", i)
		case nil:
			fmt.Printf("param #%d is nil\n", i)
		case string:
			fmt.Printf("param #%d is a string\n", i)
		case p5_1_typeOper.Student:
			fmt.Printf("param #%d is my p5_1_typeOper.Student\n", i)
		default:
			fmt.Printf("param #%d  's  type is unknow\n", i)
			
		}
		
	}
}

func Main() {
	
	fmt.Printf("beging \n")
	case1_expression()
	case2_type(5, -17.9, "ZIP", nil, true, complex(1, 1), p5_1_typeOper.Student{Name: "asdf", Age: 11, Grade: 121})
	
}
