/*
-*- coding: utf-8 -*-
--------------------------------------------------
 File Name: tMap.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-10-下午5:46
---------------------说明--------------------------
 map映射学习
---------------------------------------------------
*/

package tMap

import (
	"fmt"
)

// 因为映射属于引用类型，所以不管一个映射保存了多少数据，传递都是很廉价的（在64 位机器上只需要8个字节，在32位机器上只需要4字节）。
func case1_create() {
	// 由于[]byte是一个切片，不能作为映射的键，但是我们可以先将[]byte转换成字符串，例如string([]byte)，然后作为映射的键字段，等有需要的时候再转换回来，这种转换并不会改变原有切片的数据。
	tbyte := []byte{216, 217}
	tbyte2 := []byte{215, 218}
	tbyte_str := string(tbyte)
	tbyte_str2 := string(tbyte2)
	fmt.Printf("%v,%v \n", tbyte_str, tbyte_str2)
	// 创建map的几种方式
	// 映射的创建方式如下：
	// 1. make(map[KeyType]ValueType, initialCapacity)
	// 2. make(map[KeyType]ValueType)
	// 3. map[KeyType]ValueType{}
	// 4. map[KeyType]ValueType{key1: value1, key2: value2,..., keyN: valueN}
	//
	tmap1 := make(map[string][]byte, 2)
	tmap1[tbyte_str] = tbyte
	tmap1[tbyte_str2] = tbyte2
	tmap1["test"] = []byte{123, 123, 123}
	fmt.Printf("map数据集合:%v \n", tmap1)
	//
	tmap2 := make(map[string]string)
	tmap2["author"] = "hanxu"
	tmap2["github"] = "github.com/thesunboy-com"
	fmt.Printf("map2数据集合:%v \n", tmap2)
}

func Main() {
	case1_create()
}
