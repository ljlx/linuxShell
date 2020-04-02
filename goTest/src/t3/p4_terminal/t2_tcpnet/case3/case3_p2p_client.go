/*
--------------------------------------------------
 File Name: case3_p2p_client.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-16-下午3:50
---------------------说明--------------------------
 客户端
---------------------------------------------------
*/

package case3_p2p

import (
	"encoding/json"
	"fmt"
	"math/rand"
	"net"
	"strconv"
	"strings"
	"time"
)

var (
	vtagname = ""
)

type ClientPeerMsg struct {
	CliName string "客户端tag"
	CliIp   string "客户端一些环境,ip"
	CliPort int    "客户端一些环境,port"
	CliMsg  string "客户端想说的信息"
}

func (client *ClientPeerMsg) ToJsonStr() string {
	if jsonbyte, err := json.Marshal(client); err != nil {
		loginfo.Printf("格式化json错误==>%v, errmsg:%v \n", client, err)
		return ""
	} else {
		jsonstr := string(jsonbyte)
		return jsonstr
	}
}

/*
get rand for a<x<b
*/
func getRandn(a, b int) (x int) {
	intn := rand.Intn(b - a)
	return intn + a
}

// 测试p2p的客户端进程.
func Mainp2pClient(tagname string) {
	
	clientPeerMsg := new(ClientPeerMsg)
	clientPeerMsg.CliIp = net.IPv4zero.String()
	clientPeerMsg.CliPort = getRandn(8800, 9000)
	clientPeerMsg.CliName = tagname
	clientPeerMsg.CliMsg = "hello,iam a client peers"
	//
	vtagname = tagname
	srcaddr := &net.UDPAddr{IP: net.IPv4zero, Port: 9999}
	serverIP := "47.52.94.171"
	serverPort := 8088
	
	dstaddr := &net.UDPAddr{
		IP:   net.ParseIP(serverIP),
		Port: serverPort,
	}
	dialUDPConn, err := net.DialUDP("udp", srcaddr, dstaddr)
	if err != nil {
		logerr.Fatalf("连接udp服务器[]失败,err:%v \n ", dstaddr, err)
	}
	// hellomsg := fmt.Sprintf("hello,iam a client peers:%v", tagname)
	hellomsg := clientPeerMsg.ToJsonStr()
	if _, err := dialUDPConn.Write([]byte(hellomsg)); err != nil {
		logerr.Fatalf("写入失败==> \n")
	}
	peerData := make([]byte, 1024)
	// TODO  这里应该是服务端发送的另个客户端的消息.
	if n, remoteAddr, err := dialUDPConn.ReadFromUDP(peerData); err != nil {
		logerr.Fatalf("==>client[%v],read err :%v \n", remoteAddr, err)
	} else {
		peerMsg := peerData[:n]
		peerAddrStr := string(peerMsg)
		otherPeerUdpAddr := parseAddr(peerAddrStr)
		loginfo.Printf("local:%v server:%v another:%v \n", srcaddr, remoteAddr, otherPeerUdpAddr)
		loginfo.Printf("==>server[%v],read size of[%d]data:%v \n", remoteAddr, n, peerAddrStr)
		dialUDPConn.Close()
		// 开始进行打洞.
		bidirectionHold(srcaddr, &otherPeerUdpAddr)
	}
}

/*
和对方client地址进行打洞.
*/
func bidirectionHold(local *net.UDPAddr, otherPeer *net.UDPAddr) (err error) {
	udpConn, err := net.DialUDP("udp", local, otherPeer)
	if err != nil {
		logerr.Printf("失败.%v \n ", err)
		return err
	}
	defer udpConn.Close()
	//    // 向另一个peer发送一条udp消息(对方peer的nat设备会丢弃该消息,非法来源),用意是在自身的nat设备打开一条可进入的通道,这样对方peer就可以发过来udp消息
	if _, err := udpConn.Write([]byte("hi,hold")); err != nil {
		loginfo.Printf("udpConn.Write==>send handshake:hi,hold. %v \n", err)
	}
	go func() {
		for true {
			time.Sleep(10 * time.Second)
			if n, err := udpConn.Write([]byte(fmt.Sprintf("from [%v] ", vtagname))); err != nil {
				loginfo.Printf("==>send msg fail %v \n", err)
			} else {
				loginfo.Printf("==>send msg success %v \n", n)
				
			}
		}
	}()
	
	for true {
		databytes := make([]byte, 1024)
		if i, addr, err := udpConn.ReadFromUDP(databytes); err != nil {
		
		} else {
			loginfo.Printf("收到peer[%v]数据,打洞成功==>%v \n", addr, databytes[:i])
			
		}
	}
	return err
}

func parseAddr(addr string) net.UDPAddr {
	t := strings.Split(addr, ":")
	port, _ := strconv.Atoi(t[1])
	return net.UDPAddr{
		IP:   net.ParseIP(t[0]),
		Port: port,
	}
}
