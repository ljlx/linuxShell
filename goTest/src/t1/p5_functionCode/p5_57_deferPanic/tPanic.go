/*
--------------------------------------------------
 File Name: tPanic.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-21-下午5:54
---------------------说明--------------------------
 panic
---------------------------------------------------
*/

package deferPanic

import (
	"errors"
	"fmt"
	"log"
	"math"
	"net/http"
	"os"
	"strconv"
)

/*
通过内置的panic()和recover()函数，Go语言提供了一套异常处理机制。类似于其他语言（例如，C++、Java和Python）中所提供的异常机制，这些函数也可以用于实现通用的异常处理机制，，但是这样做在Go语言中是不好的风格。
 */

func afterCheck(chushu, beichushu int) (resu int, err error) {
	if chushu > 0 {
		resu = beichushu / chushu
	} else {
		return 0, errors.New("除数不能为0.")
	}
	defer func() {
		mochu := resu % chushu
		
		if mochu == 0 {
			// this is right
		} else {
			// 另一种使用案例是，将类似panic(＂unreachable＂)这样的调用放在一个我们从逻辑上判断不可能到达的地方（例如函数的末尾，而该函数总是会在到达末尾之前通过return语句返回），或者在一个前置或者后置条件被破坏时才调用panic()函数。这样做可以保证，如果我们破坏了函数的逻辑，立马就能够知道。
			panic(fmt.Sprintf("this is error.%v / %v = %v \n", beichushu, chushu, resu))
		}
	}()
	return resu, nil
}

func catchPanic(function func()) {
	defer func() {
		// dealError
		// 另一种解决方案是，我们完成必要的清理工作，然后手动调用 panic()函数来让该异常继续传播。一个通用的解决方案是，创建一个 error值，并将其设置成包含了recover()调用的函数的返回值（或返回值之一），这样就可以将一个异常（即一个panic()）转换成错误（即一个error）。
		errinfo := recover()
		if errinfo != nil {
			// do some thing clean
			errorinfo := fmt.Errorf("recoverError:%v", errinfo)
			fmt.Fprintf(os.Stderr, "捕获的异常:%v", errorinfo)
		}
		
	}()
	function()
}

func MainPanic() {
	// ----------start----------丑陋的捕捉异常----------start----------
	defer func() {
		// dealError
		// 另一种解决方案是，我们完成必要的清理工作，然后手动调用 panic()函数来让该异常继续传播。一个通用的解决方案是，创建一个 error值，并将其设置成包含了recover()调用的函数的返回值（或返回值之一），这样就可以将一个异常（即一个panic()）转换成错误（即一个error）。
		errinfo := recover()
		if errinfo != nil {
			// do some thing clean
			errorinfo := fmt.Errorf("recoverError:%v", errinfo)
			fmt.Fprintf(os.Stderr, "捕获的异常:%v", errorinfo)
		}
		
	}()
	// ----------end------------丑陋的捕捉异常----------end------------
	result, _ := afterCheck(2, 8)
	fmt.Printf("this is right:%v \n", result)
	
	result, err := afterCheck(0, 8)
	fmt.Printf("this is error:%v ,error: %v \n", result, err)
	
	// Go语言将错误和异常两者区分对待。错误是指可能出错的东西，程序需以优雅的方式将其处理（例如，文件不能被打开）。而异常是指“不可能”发生的事情（例如，一个应该永远为true的条件在实际环境中却是false的）。
	// 比如在自己封装的类型, 或者是json结构中,被其他开发人员复写一些方法时,错误的实现,给破坏了一个对象,类值的状态,进行后置校验的函数.
	// 这非常类似一个断言.
	// 这个时候 我们应该调用panic来抛出这个异常,尽早的解决错误.
	
	// catchPanic(afterCheck(2, 1))
	
	result, err = afterCheck(3, 8)
	fmt.Printf("this is panic.%v,panic: %v \n", result, err)
	
	// 最简单同时也可能是最好的方法是调用 panic()函数来中断程序的执行以强制发生错误，使得该错误不会被忽略因而能够被尽快修复。
	// 但是!!!
	// 一旦开始部署程序时，任何情况下可能发生错误都应该尽一切可能避免中断程序。我们可以保留所有 panic()函数但在包中添加一个延迟执行的recover()调用来达到这个目的。在恢复过程中，我们可以捕捉并记录任何异常（以便这些问题保留可见），同时向调用者返回非nil的错误值，而调用者则会试图让程序恢复到健康状态并继续安全运行。
	// 比如一个web服务,后台服务, 我们不希望它突然就进程结束了,就因为一个错误的业务逻辑,而影响了其他的功能,这个时候我们需要捕获这个异常,并恢复程序的状态.
	
	// 	如果其中有个延迟执行的函数或者方法包含一个对内置的recover()函数（可能只在一个延迟执行的函数或者方法中调用）的调用，该异常展开过程就会终止
	
	// 1. 这种情况下，我们就能够以任何我们想要的方式响应该异常。有种解决方案是忽略该异常，这样控制权就会交给包含了延迟执行的recover()调用的函数，该函数然后会继续正常执行。我们通常不推荐这种方法，但如果使用了，至少需要将该异常记录到日志中以不完全隐藏该问题
	
}

// 以下来自书中的例子.

/*
抛出异常,结束程序.
 */
func ConvertInt64ToInt(x int64) int {
	if math.MinInt32 <= x && x <= math.MaxInt32 {
		return int(x)
	}
	// 	否则无法合法的向下转换的int64,抛出异常.
	panic(fmt.Errorf("cann't convert int64[%v] to int32 \n", x))
}

func IntFromInt64(x int64) (i int, err error) {
	defer func() {
		if e := recover(); e != nil {
			err = fmt.Errorf("%v", e)
			// 该函数被调用时，Go语言会自动地将其返回值设置成其对应类型的零值，如在这里是0和nil
		}
	}()
	i = ConvertInt64ToInt(x)
	return i, nil
	
}

func http_helloPanic(response http.ResponseWriter, request *http.Request) {
	
	request.ParseForm()
	intstr := request.FormValue("intv")
	fmt.Printf("解析http-get-params:%v \v \n", intstr)
	intv, _ := strconv.ParseInt(intstr, 10, 64)
	intv32 := ConvertInt64ToInt(intv)
	fmt.Printf("success convert 64 to 32, %v \n", intv32)
}

func http_error_handle(function func(http.ResponseWriter, *http.Request)) (func(http.ResponseWriter, *http.Request)) {
	
	return func(writer http.ResponseWriter, request *http.Request) {
		
		defer func() {
			// 捕获一个网页的异常,每个func 都需要, 这也太麻烦了吧/px,别急,下面会解决
			if httperr := recover(); httperr != nil {
				// log.Panicf("[500],ClientIp[%s]-http服务器遇到了一个问题:%v", request.RemoteAddr, httperr)
				log.SetOutput(os.Stdout)
				log.Printf("[500],ClientIp[%s]-http服务器遇到了一个问题:%v", request.RemoteAddr, httperr)
				log.SetOutput(writer)//全局设置,相当于单例模式,本次修改会影响到整个http服务器,并不是对当前的输出流进行改变,和java的spring无状态服务不一样
				log.Printf("[500],内部服务器错误.%v", request.RemoteAddr)
			}
		}()
		
		function(writer, request)
		
	}
	
}

func Main_http_panic() {
	http.HandleFunc("/", http_error_handle(http_helloPanic))
	http.ListenAndServe("localhost:9090", nil)
}
