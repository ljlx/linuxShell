# Go语言其他知识速记

## 编译
> 编译分为动态链接编译和静态库编译.  Go语言默认是使用静态库编译.
1. 动态编译
2. 静态编译  
> 按照不同平台又可划分为本地平台编译和交叉编译
1. [本地编译](#本地编译)
2. [交叉编译](#交叉编译)


#### 本地编译

* 编译生成本地平台二进制可执行文件, 不执行
```
    go build main.go
```

* 在本地临时目录,编译生成二进制可执行文件,并执行
```
    go run main.go
```

* 下载远程环境的包
```
    go get github.com/thesunboy-com/linuxShell/goTest
```

#### 交叉编译
> Golang 支持交叉编译，在一个平台上生成另一个平台的可执行程序，最近使用了一下，非常好用，这里备忘一下。
> GOOS：目标平台的操作系统（darwin、freebsd、linux、windows）
  GOARCH：目标平台的体系架构（386、amd64、arm）
  交叉编译不支持 CGO 所以要禁用它
  
* Mac 下编译 Linux 和 Windows 64位可执行程序
```
    CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build main.go
    CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build main.go
```

* Linux 下编译 Mac 和 Windows 64位可执行程序
```
CGO_ENABLED=0 GOOS=darwin GOARCH=amd64 go build main.go
CGO_ENABLED=0 GOOS=windows GOARCH=amd64 go build main.go
CGO_ENABLED=0 GOOS=windows GOARCH=386 go build main.go
```
* Windows 下编译 Mac 和 Linux 64位可执行程序
```
SET CGO_ENABLED=0
SET GOOS=darwin
SET GOARCH=amd64
go build main.go

SET CGO_ENABLED=0
SET GOOS=linux
SET GOARCH=amd64
go build main.go
```


#### Go环境变量
> 执行`go env` 可以查看本地go环境变量
```
GOARCH="amd64"
GOBIN=""
GOCACHE="/home/hanxu/.cache/go-build"
GOEXE=""
GOHOSTARCH="amd64"
GOHOSTOS="linux"
GOOS="linux"
GOPATH="/home/hanxu/.GO/thirdPkg:/usr/linuxShell/goTest/:/home/hanxu/.GO/target:/tmp/GO/target"
GORACE=""
GOROOT="/usr/lib/go"
GOTMPDIR=""
GOTOOLDIR="/usr/lib/go/pkg/tool/linux_amd64"
GCCGO="gccgo"
CC="gcc"
CXX="g++"
CGO_ENABLED="1"
CGO_CFLAGS="-g -O2"
CGO_CPPFLAGS=""
CGO_CXXFLAGS="-g -O2"
CGO_FFLAGS="-g -O2"
CGO_LDFLAGS="-g -O2"
PKG_CONFIG="pkg-config"
GOGCCFLAGS="-fPIC -m64 -pthread -fmessage-length=0 -fdebug-prefix-map=/tmp/go-build710718011=/tmp/go-build -gno-record-gcc-switches"
```


### 减少GO二进制程序体积

可以发现由 ```go build xxx.go``` 编译出来的可执行程序体积较大,不利于空间的有效利用.   
>那么有什么好用的办法可以减少包的体积呢?

1. **编译参数的优化**
2. **使用加壳技术**

#### 原因分析
> 参考 [golang语言编译的二进制可执行文件为什么比 C 语言大](https://www.cnxct.com/why-golang-elf-binary-file-is-large-than-c/)

众所周知(我就不知道/wn)，linux 上的二进制可执行文件是 ``` ELF  (Executable and Linkable Format)``` 可执行和可链接格式

ELF 文件分为如下：
 * ELF文件的组成：ELF header
 * 程序头：描述段信息
 * Section头：链接与重定位需要的数据
 * 程序头与Section头需要的数据.text .data

在 Linux 上， 查看elf格式构成可以使用 ```hanxu@hx-mint#  readelf -h go-bin-file.out```

 ELF 头的长度都是一样的，不会带来总体体积的变化。区别是个别字节的值不一样，比如Entry point address 程序入口点的值不一样等.
 
 接下来是 程序头：，也就是 section部分（在linker连接器的角度是section部分或者装载器角度的segment）

> 另外,.gopclntab 跟 .gosymtab段的讨论，以及其他建议

    https://groups.google.com/forum/#!topic/golang-dev/EJhwBrITcpA
    https://groups.google.com/forum/#!msg/golang-dev/EJhwBrITcpA/EMHeWpriGZUJ
    如果想要ELF二进制程序变小的方法，还可以使用 linux 的strip，以及 UPX 来压缩 ELF 文件。
    推荐一本书《程序员的自我修养-链接、装载与库》链接

