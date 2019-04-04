package io

import (
	"os"
	"bufio"
	"io"
)

type testttt interface {
	test() string
}

func testInterfaceReader(reader io.Reader) {
	//b := []byte{1024}
	//reader.Read(b)
	return
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

func GetInputText() string {
	bufinreader := bufio.NewReader(os.Stdin)
	if bytes, _, err := bufinreader.ReadLine(); err == nil {
		return string(bytes)
	}
	return ""
}
