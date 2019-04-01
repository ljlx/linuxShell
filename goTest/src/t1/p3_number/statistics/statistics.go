/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: statistics.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-1-上午10:05
---------------------说明--------------------------
 2.4 例子：statistics
---------------------------------------------------
*/

package statistics

import (
	"sort"
	"net/http"
	"fmt"
	"log"
	"os"
	"bytes"
	"strings"
	"strconv"
)

/*
2.4 例子：statistics

这个例子的目的是为了提高大家对Go编程的理解并提供实践机会。就如同第一章，这个例子使用了一些还没有完整讲解的Go语言特性。这应该不是大问题，因为我们提供了相应的简单解释和交叉引用。这个例子还很简单的使用了 Go语言官方网络库 net/http 包。使用net/http包我们可以非常容易地创建一个简单的HTTP服务器。最后，为了不脱离本章的主题，这节的例子和练习都是数值类型的。

statistics程序（源码在statistics/statistics.go文件里）是一个Web应用，先让用户输入一串数字，然后做一些非常简单的统计计算，如图 2-2 所示。我们分两部分来讲解这个例子，先介绍如何实现程序中相关的数学功能，然后再讲解如何使用net/http包来创建一个Web应用程序。由于篇幅有限，而且书中的源码均可从网上下载，所以有侧重地只显示部分代码（对于import部分和一些常量等可能会被忽略掉），当然，为了让大家能更好地理解我们会尽可能讲解得全面些。
 */
//-----------------------结构体,常量定义---------------------------
//1.常量定义

const (
	html_pageTop          = "<html><body>"
	html_form             = "<form action = \"/\" method = \"POST\">" + "<label for = \"numbers\">Numbers comma or space-separated):</label><br />" + "<input type = \"text\" name = \"numbers\" size = \"30\"><br />" + "<input type = \"submit\" value = \"Calculate\">" + "</form>"
	html_pageBottom       = "</body></html>"
	html_template_message = "<p class=\"error\">%s</p>"
	html_table            = "<table border=\"1\">" + "<tr><th colspan=\"2\">Results</th></tr>" + "<tr><td>Numbers</td><td>%v</td></tr>" + "<tr><td>Count</td><td>%d</td></tr>" + "<tr><td>Mean</td><td>%f</td></tr>" + "<tr><td>Median</td><td>%f</td></tr>" + "</table>"
)

//2.结构体

/*
包含用户输入的数据以及我们准备计算的两种统计

Go语言里的结构体类似于C里的结构体或者Java里只有public数据成员的类（不能有方法），但是不同于C++的结构体，因为它并不是一个类
 */
type hxStatistics struct {
	numbers []float64
	/*
	平均数
	 */
	meanAvg float64

	/*
	中位数
	 */
	mdian float64
}

//-------------------------结构体,常量定义------------------------------

// ----------start----------私有方法----------start----------

func testPrivate() {

}

/*
	求和运算
 */
func sum(numbers []float64) (total float64) {
	for _, x := range numbers {
		total += x
	}
	return total
}

/*
计算中位数
 */
func median(numbers []float64) float64 {

	middle := len(numbers) / 2
	result := numbers[middle]
	if len(numbers)%2 == 0 {
		result = (result + numbers[middle-1]) / 2
	}
	return result
}

func getStats(numbers []float64) (stats hxStatistics) {
	stats.numbers = numbers
	//sort函数修改了入参,调用者的值也被改了,因为他们是按引用/指针传递的,这种情况在传切片、引用或者函数指针到函数时是很常见的
	//如果需要保留原始切片,那就使用copy()函数
	//sort包里的Float64s()函数对原数组进行升序排列（原地排序）
	sort.Float64s(stats.numbers)

	pNumberSUM := sum(stats.numbers)
	//使用内置的len()取得切片的大小（总个数）并将其强制转换成float64类型的变量（因为sum()函数返回一个float64的值）
	pNumbersLen := float64(len(stats.numbers))
	////我们没有检查除数(pNumbersLen)为0的情况，因为在我们的程序逻辑里，getStats()函数只有在至少有1个数据的时候才会被调用，否则程序会退出并产生一个运行时异常（runtime panic）
	//	//在这里是
	stats.meanAvg = pNumberSUM / pNumbersLen

	stats.mdian = median(stats.numbers)
	return stats
}

// ----------end------------私有方法----------end------------

// ----------start----------public func----------start----------

// ----------end------------public func----------end------------

// ----------start----------http handler----------start----------

func processParseRequest(request *http.Request) ([]float64, string, bool) {
	var numbers []float64
	slice, found := request.Form["numbers"]
	if found && len(slice) > 0 {
		sliceItem := slice[0]
		text := strings.Replace(sliceItem, ",", " ", -1)
		for _, field := range strings.Fields(text) {
			if x, err := strconv.ParseFloat(field, 64); err != nil {
				return numbers, "'" + field + "' is invalid", false
			} else {
				numbers = append(numbers, x)
			}
		}
	}
	if len(numbers) == 0 {
		return numbers, "111", false // 第一次get请求,没有数据被显示,不是一个错误.
	}
	return numbers, "222", true
}

func http_homepage(writer http.ResponseWriter, request *http.Request) {
	//如何代理实现?
	fmt.Println("start http request [/]...")
	error := request.ParseForm() // 必须在写响应内容之前调用
	fmt.Fprint(writer, html_pageTop, html_form)
	if error != nil {
		return
	}
	if numbers, message, ok := processParseRequest(request); ok {
		mStats := getStats(numbers)
		fmt.Fprintf(writer, html_template_message, formatStats(mStats))
	} else if message != "" {
		fmt.Fprintf(writer, html_template_message, message)
	}
	formvalues := request.FormValue("numbers")
	println(formvalues)
	fmt.Fprint(writer, html_pageBottom)
	fmt.Println("end http request [/]...")
}

/*
	格式化 统计信息 结构体数据
 */
func formatStats(stats hxStatistics) string {

	return fmt.Sprintf(html_table, stats.numbers, len(stats.numbers), stats.meanAvg, stats.mdian)

}

func http_err_404(w http.ResponseWriter, r *http.Request) {
	textBytes := bytes.NewBufferString("this is my 404").Bytes()
	w.Write(textBytes)
	w.WriteHeader(404)
}

// ----------end------------http handler----------end------------

func DoStatisTest() {
	if currProcess, err := os.FindProcess(os.Getpid()); err == nil {
		println("os.Getpid()", os.Getpid())
		hostname, _ := os.Hostname()
		println("os.Hostname()", hostname)
		println(currProcess)
	}
	//这个函数的签名必须是func(http.ResponseWriter, *http.Request)我们可以注册多个“路径-函数”对，这里我们只注册了“/”（通常是网页程序的主页）和一个自定义的homePage()函数。

	http.HandleFunc("/", http_homepage)
	http.HandleFunc("/err404", http_err_404)
	//http.ListenAndServe()的第二个参数支持自定义的服务器，为空的话（传一个nil参数）表示使用默认的类型。
	if err := http.ListenAndServe(":9001", nil); err != nil {
		log.Fatalf("failed to start server,the resason:", err)
	}
}
