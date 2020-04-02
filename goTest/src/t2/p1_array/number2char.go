package main

import (
	"fmt"
	"log"
	"path/filepath"
)

func run() {
	fmt.Println("学习go语言数组切片")
	var strarray = [][]string{
		{"　000 ",
			" 0　　0 ",
			"0　　 0",
			"0　　 0",
			"0　　 0",
			" 0　　0 ",
			"　000 "},
		{
			" 1 ",
			"11 ",
			" 1 ",
			" 1 ",
			" 1 ",
			" 1 ",
			"111"},
		{
			" 222 ",
			"2　 2",
			"　　2 ",
			"　 2 ",
			"　2 ",
			"2 ",
			"22222"},
		{
			" 9999",
			"9　 9",
			"9　　9",
			" 9999",
			"　　9",
			"　 9",
			"　9",
			"9",
		},
	}

	stringOfDigits := [] int{48, 51}
	for row := range strarray[0] {
		line := " "
		for column := range stringOfDigits {
			digit := stringOfDigits[column] - '0'
			if 0 <= digit && digit <= 9 {
				line += strarray[digit][row] + " "
			} else {
				log.Fatal("invalid whole number")
			}

		}
		fmt.Println(line)
	}

}

func stringprint() {
	var strarray = [][]string{
		{"　000 ",
			" 0　　0 ",
			"0　　 0",
			"0　　 0",
			"0　　 0",
			" 0　　0 ",
			"　000 "},
		{" 1 ", "11 ", " 1 ", " 1 ", " 1 ", " 1 ", "111"},
		{" 222 ", "2　 2", "　　2 ", "　 2 ", "　2 ", "2 ", "22222"},
		{" 9999", "9　 9", "9　　9", " 9999", "　　9", "　 9", "　　9"},
	}
	fmt.Println(strarray)
	fmt.Printf("【%v】", filepath.Base("/home/lijie"))
	if len(strarray) == 1 {
		fmt.Printf("usage:%<whole-number>\n", filepath.Base(strarray[0][0]))
	}
}
