/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: hxfmt.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-4-下午12:45
---------------------说明--------------------------
 fmt的一些使用.
---------------------------------------------------
*/

package hxfmt

import "fmt"

func Errorf() {
	a := "sdfsdf"
	b := &a
	fmt.Printf("%v %v", *b, b)
}

func Fprint() {

}
