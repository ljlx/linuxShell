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
	// 1.
	tmap1 := make(map[string][]byte, 2)
	tmap1[tbyte_str] = tbyte
	tmap1[tbyte_str2] = tbyte2
	tmap1["test"] = []byte{123, 123, 123}
	fmt.Printf("map数据集合:%v \n", tmap1)
	fmt.Printf("取出字节字符串(215, 218), %v \n", tmap1[string(tbyte2)])
	// 由于map的key不能用切片,但是通过某些办法可以绕过.这里使用字节切片的时候,转换成字符串,然后存进map,虽然看起来随意的字节切片转换为字符串是错误乱码的,但是map依然能按照字符串实际的字节信息来正确取出对应的value
	//
	tmap2 := make(map[string]string)
	tmap2["author"] = "hanxu"
	tmap2["github"] = "github.com/thesunboy-com"
	fmt.Printf("map2数据集合:%v \n", tmap2)
	// 2.
	// 对于一些比较小的映射，我们没必要考虑是否要指定它们的初始容量，但如果这个映射比较大，指定恰当的容量可以提高性能。通常如果你知道它的容量的话最好就指定它，即使是近似的也好
	testmap := make(map[string]int)
	testmap["test1"] = 123
	testmap["pi"] = 314
	delete(testmap, "pi")
	fmt.Printf("map: %v \n")
	// 3.& 4
	emptymap := map[string]string{}
	emptymap["initemptymap"] = "lalala"
	initmap := map[string]string{"initkey": "initvalue", "initkey2": "initvalue2"}
	fmt.Printf("init map: %v \n", initmap)
	
}

type foodmush struct {
	id    int
	money float32
	name  string
}

func (foodself foodmush) String() string {
	return fmt.Sprintf("name:[%v],money:[%v]", foodself.name, foodself.money)
}

func mapPoint() map[string]float32 {
	foodMoney := make(map[string]float32)
	foodMoney["apple"] = 3.14
	foodMoney["oranage"] = 6.34
	foodMoney["apple"] = 3.141592653
	foodmap := make(map[*foodmush]string)
	foodmap[&foodmush{1, 2.35, "大米"}] = "大米v"
	mianfenFood := foodmush{2, 6.7, "面粉"}
	foodmap[&mianfenFood] = "面粉"
	mianfenFood.name = "面粉名字修改."
	fmt.Printf("没有使用指针的map[foodmuch],内存地址:%p %v \n", foodmap, foodmap)
	
	return foodMoney
}

func mapSearch() {
	foodmap := mapPoint()
	if apple, found := foodmap["apple"]; found {
		fmt.Printf("apple->%v \n", apple)
	} else {
		// TODO Errorf 无法在控制台输出 why?
		fmt.Printf("apple not found:%2f \n", apple)
	}
}

func Main() {
	case1_create()
	// mapPoint()
	mapSearch()
}
