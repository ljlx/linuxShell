package io

import (
	"os"
	"bufio"
)

type testttt interface {
	test() string
}


func testreader(filename string) {
	if fileinput, err := os.Open(filename); err != nil {
		println(fileinput)
		bufreader := bufio.NewReader(fileinput)
		isloop := true
		for isloop {
			if linebyte, isPrefix, err2 := bufreader.ReadLine(); err2 != nil {
				println(isPrefix)
				println(linebyte)
			}
		}

	}

}
