/*
--------------------------------------------------
 File Name: case1_tcpnet.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-14-上午9:01
---------------------说明--------------------------

---------------------------------------------------
*/

package case1

import (
	"bufio"
	"fmt"
	"golang.org/x/crypto/ssh/terminal"
	"io"
	"log"
	"net"
	"os"
	"reflect"
	"strings"
	"time"
)

var loginfo = log.New(os.Stdout, "[info]:", log.LstdFlags)
var logerr = log.New(os.Stderr, "[err]:", log.LstdFlags)

func GetTestReader() func() {
	reader := bufio.NewReader(os.Stdin)
	testreader := func() {
		for {
			
			line, isprefex, err := reader.ReadLine()
			loginfo.Printf("==>line:%v ,isprefix:%v, err:%v \n", line, isprefex, err)
		}
	}
	loginfo.Printf("==> %v \n", reflect.TypeOf(testreader))
	return testreader
}

func ServerListener(addr *net.TCPAddr) (ok bool, err error) {
	var (
		tcpListener net.Listener
	)
	if addr == nil {
		addr = new(net.TCPAddr)
		addr.IP = net.IPv4(0, 0, 0, 0)
		addr.Port = 44444
		
	}
	isok := make(chan bool, 1)
	go func(startOk chan bool) {
		if tcpListener, err = net.ListenTCP("tcp", addr); err != nil {
			logerr.Fatalf("ServerListener==>监听服务器端口失败%v \n", addr)
		}
		startOk <- true
		//
		for {
			conn, err := tcpListener.Accept()
			if err != nil {
				logerr.Printf("accept==>建立连接失败 \n")
			}
			logerr.Printf("accept==>建立连接成功... \n")
			terminalnew := terminal.NewTerminal(conn, ">")
			terminalnew.Write([]byte(fmt.Sprintf("hello. you ip:%v \n", conn.RemoteAddr())))
			go func(cliTerminal *terminal.Terminal) {
				defer conn.Close()
				for {
					line, err := cliTerminal.ReadLine()
					
					if err != nil {
						if err != io.EOF {
							logerr.Fatalf("terminal==> cliTerminal.ReadLine has been err:%v \n", err)
						}
					} else {
						cliTerminal.Write([]byte(fmt.Sprintf("you resp:%v\n", line)))
					}
					
				}
			}(terminalnew)
			
			serverTest := func(cliTerminal *terminal.Terminal) {
				reader := bufio.NewScanner(os.Stdin)
				for {
					// defer reader.Close()
					builder := new(strings.Builder)
					for reader.Scan() {
						builder.WriteString(reader.Text())
					}
					line := builder.String()
					time.Sleep(time.Second * 2)
					loginfo.Printf("==>%v \n", line)
					
					if err != nil {
						if err != io.EOF {
							logerr.Printf("os==> cliTerminal.ReadLine has been err:%v \n", err)
						}
					} else if strings.TrimSpace(line) != "" {
						cliTerminal.Write([]byte(fmt.Sprintf("server resp:%v\n", line)))
					}
					
				}
			}
			loginfo.Printf("serverTest协程==> %v \n", reflect.TypeOf(serverTest))
			//
			testReader := GetTestReader()
			testReader()
			
		}
	}(isok)
	for {
		if <-isok {
			loginfo.Printf("ServerListener==> 开启服务器成功 \n")
			// return true, nil
		} else {
			logerr.Printf("ServerListener==> 开启服务器失败 \n")
			return false, err
		}
		
	}
	
}
