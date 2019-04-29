/*
--------------------------------------------------
 File Name: init.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-28-下午6:02
---------------------说明--------------------------

---------------------------------------------------
*/

package tInit

import (
	"fmt"
	"runtime"
)

func init() {
	curversion := runtime.Version()
	fmt.Printf("包[%s],init函数初始化,go-version:%s \n", "tInit ", curversion)
}

func multParams(args ...string) {
	fmt.Printf("可变参数:%v", args)
}

func Main() {
	fmt.Printf("main...")
	multParams("21", "123", "j90")
	
}
