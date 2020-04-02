/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: main.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-8-下午2:04
---------------------说明--------------------------

---------------------------------------------------
*/

package main

import (
	"t1/p4_collect/point"
	"fmt"
	"t1/p4_collect/p42_arraySlice"
	"t1/p4_collect/p43_map"
)

func main() {
	point.TestMain()
	arraySlice.Main()
	tMap.Main()
	fmt.Println("test finish.now exit")
}
