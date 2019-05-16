/*
--------------------------------------------------
 File Name: case3_p2p_server.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-16-下午2:34
---------------------说明--------------------------

---------------------------------------------------
*/

package case3_p2p

import (
	"log"
	"net"
	"os"
	"time"
)

var loginfo = log.New(os.Stdout, "[info]:", log.LstdFlags)
var logerr = log.New(os.Stderr, "[err]:", log.LstdFlags)

func Mainp2pServer() {
	listenPort := 8088
	// net.IPv4zero
	// 1. listen port with udp
	listener, err := net.ListenUDP("udp", &net.UDPAddr{IP: net.IP{0, 0, 0, 0}, Port: listenPort})
	if err != nil {
		logerr.Fatalf("%v \n ", err)
	}
	loginfo.Printf("==>服务器监听地址:%v \n", listener.LocalAddr().String())
	
	// 2. accept conn and handler it.
	for true {
		loopOpenCliConn(listener)
	}
	
}

func loopOpenCliConn(listener *net.UDPConn) {
	udpAddrsPeers := make([]net.UDPAddr, 0, 2)
	dataBytes := make([]byte, 1024)
	for {
		loginfo.Printf("服务器监听开始,等待客户端连接==> \n")
		
		n, remoteAddr, err := listener.ReadFromUDP(dataBytes)
		if err != nil {
			logerr.Printf(" error during read: %v \n ", err)
		}
		clientHelloMsg := string(dataBytes[:n])
		loginfo.Printf("==>客户端远程地址%v,读取%d个字节数据:%v \n", remoteAddr.String(), n, clientHelloMsg)
		udpAddrsPeers = append(udpAddrsPeers, *remoteAddr)
		// p2p两个客户端连上来了
		if len(udpAddrsPeers) == 2 {
			loginfo.Printf("==>进行UDP打洞, 建立%v <--> %v 的连接 \n", udpAddrsPeers[0].String(), udpAddrsPeers[1].String())
			
			listener.WriteToUDP([]byte(udpAddrsPeers[0].String()), &udpAddrsPeers[1])
			listener.WriteToUDP([]byte(udpAddrsPeers[1].String()), &udpAddrsPeers[0])
			time.Sleep(time.Second * 5)
			loginfo.Printf("==>udp打洞服务器退出,不影响peers之间的通信.. \n")
			return
		}
	}
}
