/*
--------------------------------------------------
 File Name: case1_tcpnet_test.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-14-上午9:42
---------------------说明--------------------------

---------------------------------------------------
*/

package case1_test

import (
	"bufio"
	"log"
	"net"
	"os"
	"testing"
)

var loginfo = log.New(os.Stdout, "[info]:", log.LstdFlags)
var logerr = log.New(os.Stderr, "[err]:", log.LstdFlags)

func TestServerListener(t *testing.T) {
	
	for _, unitx := range []struct {
		ip   []byte "ip address"
		port int    "port [1024-65539]"
	}{
		// 预定义结构体的一些值
		{[]byte{0, 0, 0, 0}, 1234},
	} {
		xip := unitx.ip
		xport := unitx.port
		t.Logf("test server listener: ip:%v,port:%v \n", xip, xport)
		ok, err := ServerListener(&net.TCPAddr{IP: xip, Port: xport})
		if ! ok {
			t.Fatalf("test -> 开启服务器监听测试失败:%v ,errMsg:%v \n", unitx, err)
		}
	}
	
}

func TestReadStdIn(t *testing.T) {
	reader := bufio.NewReader(os.Stdin)
	line, _, _ := reader.ReadLine()
	loginfo.Printf("==>%v \n", line)
	
}
