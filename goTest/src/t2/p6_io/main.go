package main

import (
	"fmt"
	"os"
	"log"
)

func test1() {
	infilename := "testin"
	outfilename := "testout"
	//err := nil
	infilename, outfilename, err := filenameFromCommandLine()
	if err != nil {
		fmt.Println(err)

		os.Exit(1)
	}
	println(infilename, outfilename)

	infile, outfile := os.Stdin, os.Stdout

	if outfilename != "" {
		outfile.WriteString("开始创建输出日志文件" + outfilename + "\n")
		outfile, err = os.Create(outfilename)
		if err != nil {
			log.Fatalln(err)
		}
		defer outfile.Close()
	}

	//TODO 需要有类似java-apache-common的包,判断非空.
	if infilename != "" {

		if infile, err = os.Open(infilename); err != nil {

			log.Fatalln(err)

		} else {

			//b := []uint8()

			//infile.Read(b)
		}

		defer infile.Close()

	}

	if err = americanize(infile, outfile); err != nil {

		log.Fatal(err)
	}
}

func americanize(file *os.File, file2 *os.File) interface{} {
	return nil
}

func filenameFromCommandLine() (string, string, interface{}) {
	return "/etc/hosts", "/tmp/log", nil
}

//如果某些类型包含Error() string方法或者String() string方法，Go语言的部分打印函数会使用反射功能来调用相应的函数获取打印信息

func Error() string {
	return "error info ..."
}

func String() string {
	return "go-toString()..."
}

func main() {
	test1()
}
