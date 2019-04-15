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
	"os"
	"bufio"
	"strings"
	"io"
	"encoding/json"
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

/*
类型测试的一个常用案例是处理外部数据。例如，如果我们解析JSON格式的数据，我们必须将数据转换成相对应的Go语言数据类型。这可以通过使用Go语言的json.Unmarshal()函数来实现。如果我们向该函数传入一个指向结构体的指针，该结构体又与该JSON数据相匹配，那么该函数就会将JSON数据中对应的数据项填充到结构体的每一个字段。但是如果我们事先并不知道JSON数据的结构，那么就不能给json.Unmarshal()函数传入一个结构体。这种情况下，我们可以给该函数传入一个指向interface{}的指针，这样json.Unmarshal()函数就会将其设置成引用一个map[string]interface{}类型值，其键为JSON字段的名字，而值为对应的保存为interface{}的值。
*/
func testjson() (err error) {
	jsonfilepath := "/home/hanxu/document/project/code/personal/develop/linuxShell/pyTest/test/utils-py/debug.json"
	jsonText := ""
	// ----------start----------read-json----------start----------
	if jsonfile, err := os.OpenFile(jsonfilepath, os.O_RDONLY, os.ModePerm); err == nil {
		bufreader := bufio.NewReader(jsonfile)
		strbuilder := strings.Builder{}
		for {
			bline, _, err := bufreader.ReadLine()
			goon := true
			switch err {
			case io.EOF:
				goon = false
				break
			case nil:
			default:
				return err
			}
			if !goon {
				break
			}
			strbuilder.Write(bline)
		}
		jsonText = strbuilder.String()
		fmt.Printf("jsonfile:%v", jsonText)
	}
	// ----------end------------read-json----------end------------
	var object interface{}
	jsonbyte := []byte(jsonText)
	if err := json.Unmarshal(jsonbyte, &object); err != nil {
		fmt.Printf("解析json -> interface{} error:%v \n", err)
	} else {
		// 解析json,使用map+slice
		fmt.Printf("解析json -> interface{} ,result :%v \n", object)
		// 固定返回结构,不需要使用安全类型断言
		// if jsonobject, ok := object.(map[string]interface{}); ok {
		jsonobject := object.(map[string]interface{})
		serverName := jsonobject["name"]
		serverPort := jsonobject["port"]
		serverAddTime := jsonobject["addTime"]
		serverKeepAlive := jsonobject["keepAlive"]
		serverOption := jsonobject["sshOption"]
		fmt.Printf("serverName=%v,serverPort =%v,serverAddTime =%v,serverKeepAlive =%v,serverOption =%v \n", serverName, serverPort, serverAddTime, serverKeepAlive, serverOption)
		// }
		// 使用自定义格式化输出
		formatstr := testjson_format(&jsonobject)
		fmt.Printf("(非结构体)自定义格式化输出:%v \n", formatstr)
	}
	
	return err
}

func testjson_format(jsonobject *map[string]interface{}) (output string) {
	strbuilder := strings.Builder{}
	
	//
	strbuilder.WriteString("{")
	for key, value := range *jsonobject {
		switch value.(type) {
		case bool:
			fmt.Sprintf(",%q:%t", key, value)
		case int, int8, int16, int32:
			// fmt.Fprintf(&strbuilder,)
			v := fmt.Sprintf(",%q:%d", key, value)
			strbuilder.WriteString(v)
		case float32, float64:
			v := fmt.Sprintf(",%q:%f", key, value)
			strbuilder.WriteString(v)
		case string:
			v := fmt.Sprintf(",%q:%s", key, value)
			strbuilder.WriteString(v)
		case nil:
			v := fmt.Sprintf(",%q: null", key)
			strbuilder.WriteString(v)
		case []interface{}:
			// 使用影子变量.
			fmt.Printf("影子变量内存地址测试(原始):%p,%v\n", &value, value)
			value := value.([]interface{})
			fmt.Printf("影子变量内存地址测试(影子):%p,%v\n", &value, value)
			strbuilder.WriteString("[")
			testjson_format_recursive(&strbuilder, value)
			strbuilder.WriteString("]")
		}
	}
	//
	output = strbuilder.String()
	return output
}

// func testjson_format_recursive(writer *io.Writer) {
// 	io.Writer
// TODO 面向接口编程怎么玩?
// }

// 	TODO 递归
func testjson_format_recursive(builder *strings.Builder, jsondata []interface{}) {
	// builder.WriteString("")
	for _, item := range jsondata {
		// item是一个map[string]interface{}
		// 类型断言&& 影子变量item
		if item, ok := item.(string); ok {
			text := fmt.Sprintf(", %q", item)
			builder.WriteString(text)
		}
	}
	
}

func Main() {
	
	fmt.Printf("beging \n")
	case1_expression()
	case2_type(5, -17.9, "ZIP", nil, true, complex(1, 1), p5_1_typeOper.Student{Name: "asdf", Age: 11, Grade: 121})
	testjson()
}
