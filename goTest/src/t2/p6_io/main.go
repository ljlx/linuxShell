package main

import (
	"os"
	"fmt"
	"log"
	"io"
	"bufio"
	"regexp"
	"path/filepath"
	"strings"
	"io/ioutil"
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

/**
(err error)具名返回值,
在使用具名返回值时有一个作用域的细节
 */
func americanise(inFile io.Reader, outFile io.Writer) (err error) {

	//使用装饰器模式对io对象进行修饰.类似java的io实现
	reader := bufio.NewReader(inFile)

	writer := bufio.NewWriter(outFile)

	//TO-DO 还不太明白这个, 类似py的内部def?
	//defer 在americanise函数退出后执行.
	//创建一个匿名的延迟函数，它会在americanise()函数返回并将控制权交给其调用者之前刷新writer的缓冲
	//TODO 如果有多个defer,执行顺序?
	defer func() {
		//如果想忽略任何在刷新操作之前或者在刷新操作过程中发生的任何错误，可以简单地调用defer writer.Flush()，但是这样做的话程序对错误的防御性将较低
		println("函数hook start...")
		if err == nil {
			//由于刷新缓冲区操作也可能会失败，所以我们将 writer.Flush()函数的返回值赋值给err
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

	//我们有时必须在赋值时先声明一个变量，如这里的replacer变量（标识①）和我们这里读入的line变量（标识②）。另一种可选的方式是显式地返回所有返回值，就像我们在其他地方所做的那样
	var replacer func(string) string
	//每发现一个匹配的值就调用一次 replacer 函数，并将该匹配到的文本内容替换为replacer函数返回的文本内容。

	if replacer, err = makeReplacerFunc(britishAmerican); err != nil {
		//但是如果我们在函数内部某个地方使用了if value :=...这样的语句，因为if语句会创建一个新的块，所以这个value是一个新的变量，它会隐藏掉名字同为value的具名返回值。
		//因此我们必须保证不使用快速变量声明符:=来为其赋值，以避免意外创建出一个影子变量
		return err

	}
	//使用正则匹配一个单词(用空格作为单词分隔符)
	//这个函数比较适合于正则表达式内容是从外部文件读取或由用户输入的场景，因为需要做一些错误处理。
	//regexp.Compile("[A-Za-z]+") return *regex,err
	//这个must会抛异常
	wordRx := regexp.MustCompile("[A-Za-z]+")

	//loop 条件, 类似循环是否读取到末尾,可以作为一个工具类封装起来,这点没有py方便.
	//ioutil. 不过看ioutil中,有这样的工具包.
	eof := false

	for !eof {

		var line string
		//reader.ReadLine
		line, err = reader.ReadString('\n')

		if err == io.EOF {

			err = nil // 并不是一个真正的error,只是文件末尾了

			eof = true // 在下一次迭代这会结束该循环

		} else if err != nil {

			return err // 对于真正的error，会立即结束

		}

		line = wordRx.ReplaceAllStringFunc(line, replacer)
		//如果我们有一个非常小的replacer 函数，比如只是简单地将匹配的字母转换成大写，我们可以在调用替换函数的时候将其创建为一个匿名函数,这类似与一个lambda表达式.
		line = wordRx.ReplaceAllStringFunc(line, func(word string) string { return strings.ToUpper(word) })
		//我们在这里使用了空标记符_（标识③）。这里的空标记符作为一个占位符放在需要一个变量的地方，并丢弃掉所有赋给它的值。空占位符不是一个新的变量，因此如果我们使用:=，至少需要声明一个其他的新变量
		if _, err = writer.WriteString(line); err != nil {

			return err

		}

	}

	return nil

}
func makeReplacerFunc(file string) (func(string) string, error) {
	//err := errors.New("not impl")
	rawBytes, err := ioutil.ReadFile(file)

	if err != nil {
		return nil, err
	}
	text := string(rawBytes)
	//完全看不懂这一些奇奇怪怪的字符/xk/px
	usForBritish := make(map[string]string)
	lines := strings.Split(text, "\n")
	//range xxx 相当于循环这个集合的长度的次数.
	for _, lineItem := range lines {
		//TODO
		fields := strings.Fields(lineItem)
		//Todo why is 2 ?
		if len(fields) == 2 {
			usForBritish[fields[0]] = fields[1]
		}
	}
	return func(word string) string {
		if usWord, found := usForBritish[word]; found {
			return usWord
		} else {
			return word
		}
	}, nil
	//return nil, err
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

func testInterfaceReader(reader io.Reader) []byte {
	b := []byte{9}

	bufreader := bufio.NewReader(reader)
	isloop := true
	size := 0
	//os.Create("") 源码->
	//return OpenFile(name, O_RDWR|O_CREATE|O_TRUNC, 0666)
	//twriter := nil
	//bufwriter := func(b2 []byte) io.Writer {
	//TODO 应该如何把这个if里面产生的twriter值向下传递到read块(if语句里的read代码块)中
	//如何像java那样定义一个 io.writer buufwriterObj = null;
	//var bufwriterobj bufio.Writer
	var bufwriterobj io.Writer
	//bufwriter := func() io.Writer {
	if tmpfile, err := os.OpenFile("/tmp/hosts", os.O_CREATE|os.O_APPEND|os.O_RDWR, 0600); err == nil {
		twriter := bufio.NewWriter(tmpfile)
		twriter.WriteString("fuck 怎么连初始化变量,吧这个writer带出去都不懂/xk/wn/px \n")
		//twriter.Write(b2)
		twriter.Flush()
		//TODO 如何强制转型?
		bufwriterobj = twriter
		//bufwriterobj = (bufio.Writer)twriter
		//bufwriterobj.Write([]byte{0})
		//return twriter
	}
	//return nil
	//}

	for isloop {
		//Read()方法从调用该方法的值中读取数据，并将其放到一个字节类型的切片(b)中
		//它返回成功读到的字节数(linebyte)和一个错误值(err)
		if linebyte, err := bufreader.Read(b); err == nil && linebyte != 0 {
			//如果没有错误发生，则该错误值为nil
			//如果没有错误发生但是已读到文件末尾，则返回 io.EOF。如果错误发生
			println(b[0])
			size += 1
			//TODO 不太明白这个内部func的作用和使用方法
			//我应该如何实现,在这里的read出来的字节,在写入上面创建的writer对象流中,(不使用函数签名和返回writer对象的方法.)
			bufwriterobj.Write(b)
			bufio.NewWriter(bufwriterobj).Flush()

		} else {
			if err == io.EOF {
				println("程序正常退出,io已经读到末尾,返回eof了.")
			} else {
				log.Fatalln("遇到了一个错误.", err)
			}
			isloop = false
			println(size)
		}
	}

	//TODO 如何将字节转化为字符串?
	return b
}

func testwrite(writer io.Writer, b byte) {

}

func testreader(filename string) {
	if fileinput, err := os.Open(filename); err == nil {
		println(fileinput)
		bufreader := bufio.NewReader(fileinput)
		isloop := true
		for isloop {
			if linebyte, isPrefix, err2 := bufreader.ReadLine(); err2 == nil {
				println(isPrefix)

				println(linebyte)

			} else {
				isloop = false
			}

		}

	}

}

func testIoReader() {
	//TODO	 如何调到另一个包的函数.
	if inputfile, err := os.Open("/etc/hosts"); err != nil {
		log.Fatalln(err)
	} else {
		filebyte := testInterfaceReader(inputfile)
		println(filebyte)
	}
	testreader("/etc/hosts")
}

func main() {
	testIoReader()
}
