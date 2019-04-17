# Go语言其他知识速记

## 编译

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


## Go环境变量
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