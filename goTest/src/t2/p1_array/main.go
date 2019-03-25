package main

import (
	"fmt"
	"os"
	"path/filepath"
	"log"
	"path"
)

func getarray() []string {
	weekend := []string{
		"friday",
		"saturday",
		"sunday",
		"monday",
	}
	fmt.Printf("字符数组:%s. \n", weekend)
	return weekend
}

/**
	第二个(一维切片)数组.
 */
func getarray2(i int16) []string {
	var weekend = []string{
		"friday",
		"saturday",
		"sunday",
		"monday",
	}
	fmt.Printf("字符数组:%s. \n", weekend)
	return weekend
}

/**
	二维数组
 */
func twoArray() [][]string {
	var array = [][]string{
		{"abc", "123"},
		{"def", "456"},
		{"deffg", "456", "789"},
	}
	return array
}
func filetest() {
	//filepath
}

/**
	字符编码测试 TODO 研究go编码方式.
 */
func charCode() {
	charstr := "hello"
	//'a':97, '0':48
	println("数字0的ascii:", 'a'-'0')
	for item := range charstr {
		//println(item) 0,1,2,3,4
		//range 是相当于for i:=0 ; i <= len(charstr); i++的操作.
		//取这个charstr字符的长度,作为循环的次数,因此在这个方法实例中,因为英文字符,的字节数是1,所以可以直接用charstr[item]来遍历这个字符串
		//在go语言中,byte类型等同于uint8类型 无符号8位的int,
		charbyte := charstr[item]
		println("", string(charbyte), charbyte)
		//line := ""
		//for i := 0; i <= 3; i++ {
		//	println(charstr[i])
		//}
		//println(line)
		//println("字符编码:",charstr[0],charstr[1],charstr[2],charstr[3],charstr[4],charstr[5])
		//	'我爱你'输出: 0字符编码: 230 136 145 231 136 177 228 189
		//(230 136 145,我) (231 136 177,爱)
	}
}

func parse(twoArrge [][]string) {
	if len(os.Args) == 1 {
		fmt.Printf("usage: %s <whold-number> \n", filepath.Base(os.Args[0]))
		os.Exit(1)
	}
	stringofDigits := os.Args[1]
	firstRow := twoArrge[0]
	for row := range firstRow {
		line := " "
		for column := range stringofDigits {
			ii := stringofDigits[column]
			// '0' 的(byte)uint8等于48
			digit := ii - '0'
			if 0 <= digit && digit <= 9 {
				nextline := twoArrge[digit][row]
				line += nextline + " "
			} else {
				log.Fatal("invalid whole numer.")
			}
		}
		fmt.Println(line)
	}
}

func main() {
	charCode()
	ss := getarray()
	ss2 := getarray2(1)

	env_shell := os.Getenv("PS1")
	dirlist := path.Dir("/tmp")

	fmt.Println("/tmp", dirlist)
	fmt.Println(env_shell)
	fmt.Printf("方法返回的数组:%s \n,第二个数组:%s \n", ss, ss2)
	fmt.Println(twoArray())
	fmt.Println("##----------------分割线--------------------")
	parse(twoArray())
}
