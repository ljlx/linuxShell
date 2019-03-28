package main

import (
	"os"
	"fmt"
	"log"
	"io"
	"bufio"
	"regexp"
	"path/filepath"
	"errors"
)

/**
  os.File 类型实现了 io.ReadWriter 结构（而 io.ReadWriter 是io.Reader和io.Writer 接口的组合）
 */
func getInOutFile() (*os.File, *os.File) {
	return os.Stdin, os.Stdout
}

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

	infile, outfile := getInOutFile()

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
		//任何属于defer语句所对应的语句（参见5.5节）都保证会被执行（因此需要在函数名后面加上括号），但是该函数只会在defer语句所在的函数返回时被调用。
		defer infile.Close()

	}

	if err = americanise(infile, outfile); err != nil {
		//当os.Exit()函数被直接调用或通过 log.Fatal()间接调用时，程序会立即终止，任何延迟执行的语句都会被丢失
		//Go语言的运行时系统会将所有打开的文件关闭，其垃圾回收器会释放程序的内存，而与该程序通信的任何设计良好的数据库或者网络应用都会检测到程序的崩溃，从而从容地应对
		log.Fatal(err)
	}
}

//func americanize(file *os.File, file2 *os.File) interface{} {
//
//	return nil
//}

var britishAmerican = "british-american.txt"

func americanise(inFile io.Reader, outFile io.Writer) (err error) {

	//使用装饰器模式对io对象进行修饰.类似java的io实现
	reader := bufio.NewReader(inFile)

	writer := bufio.NewWriter(outFile)

	//TODO 还不太明白这个, 类似py的内部def?
	//defer 在americanise函数退出后执行.
	defer func() {
		println("函数hook start...")
		if err == nil {

			err = writer.Flush()
		} else
		{
			println("函数hook,检测到错误.")
			writer.WriteString("错误信息:")
			writer.Flush()
			//writer.Write()
		}
		println("函数hook end...")
	}()

	//类似lambda表达式?
	var replacer func(string) string

	if replacer, err = makeReplacerFunc(britishAmerican); err != nil {

		return err

	}
	//使用正则匹配一个单词(用空格作为单词分隔符)
	wordRx := regexp.MustCompile("[A-Za-z]+")

	//loop 条件, 类似循环是否读取到末尾,可以作为一个工具类封装起来,这点没有py方便.
	//ioutil. 不过看ioutil中,有这样的工具包.
	eof := false

	for !eof {

		var line string

		line, err = reader.ReadString('\n')

		if err == io.EOF {

			err = nil // 并不是一个真正的error,只是文件末尾了

			eof = true // 在下一次迭代这会结束该循环

		} else if err != nil {

			return err // 对于真正的error，会立即结束

		}

		line = wordRx.ReplaceAllStringFunc(line, replacer)

		if _, err = writer.WriteString(line); err != nil {

			return err

		}

	}

	return nil

}
func makeReplacerFunc(s string) (func(string) string, error) {
	err := errors.New("not impl")
	return nil, err
}

/**
	处理从命令行输入的文件名.
 */
func filenameFromCommandLine() (inFilename, outFilename string, err error) {
	if len(os.Args) > 1 && (os.Args[1] == "-h" || os.Args[1] == "--help") {
		//帮助
		curfilename := os.Args[0]
		//fmt.Errorf()函数与我们之前所看的fmt.Printf()函数类似,不同之处是它返回一个错误值
		//而非将字符串输出到os.Stdout中
		//errorf函数返回一个error类型,并不直接输出到控制台中.
		err = fmt.Errorf("usage: %s [<]infile.txt [>]outfile.txt", filepath.Base(curfilename))

		return "", "", err
	} else {
		if len(os.Args) > 1 {
			inFilename = os.Args[1]
		}
		if len(os.Args) > 2 {
			outFilename = os.Args[2]
		}
	}
	if outFilename == inFilename {
		log.Fatalln("won't overwrite the infile")
	}
	return inFilename, outFilename, nil
	//return "/etc/hosts", "/tmp/log", nil
}

//如果某些类型包含Error() string方法或者String() string方法，Go语言的部分打印函数会使用反射功能来调用相应的函数获取打印信息

func Error() string {
	//errors.New函数使用一个给定的字符串来生成一个错误值

	return "error info ..."
}

func String() string {
	panic("error hanxu info")
	//还可以使用recover()函数（参见5.5节）来在其调用栈上阻止该异常的传播
	recover()

	//go 鼓励使用返回error来手动检查错误,

	//并让调用方来检查所收到的错误值。panic/recover机制的目的是用来处理真正的异常（即不可预料的异常）而非常规错误。
	return "go-toString()..."
}

func testIoReader() {
	//	 如何调到另一个包的函数.
}

func main() {
	test1()
}
