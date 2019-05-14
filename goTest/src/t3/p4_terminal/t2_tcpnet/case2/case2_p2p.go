/*
--------------------------------------------------
 File Name: case2_p2p.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-14-下午3:38
---------------------说明--------------------------
 尝试使用go建立两个内网之间的p2p连接
---------------------------------------------------
*/

package case2_p2p

import (
	"bytes"
	"log"
	"net"
	"os"
	"strconv"
	"strings"
	"testing"
)

// tcp p2p理论理解.
// https://www.cnblogs.com/snowbook/p/5133278.html

// 这里需要介绍一下NAT的类型：

// NAT设备的类型对于TCP穿越NAT,有着十分重要的影响,根据端口映射方式,NAT可分为如下4类,前3种NAT类型可统称为cone类型。
//
// (1)全克隆( Full Cone) : NAT把所有来自相同内部IP地址和端口的请求映射到相同的外部IP地址和端口。任何一个外部主机均可通过该映射发送IP包到该内部主机。
//
// (2)限制性克隆(Restricted Cone) : NAT把所有来自相同内部IP地址和端口的请求映射到相同的外部IP地址和端口。但是,只有当内部主机先给IP地址为X的外部主机发送IP包,该外部主机才能向该内部主机发送IP包。
//
// (3)端口限制性克隆( Port Restricted Cone) :端口限制性克隆与限制性克隆类似,只是多了端口号的限制,即只有内部主机先向IP地址为X,端口号为P的外部主机发送1个IP包,该外部主机才能够把源端口号为P的IP包发送给该内部主机。
//
// (4)对称式NAT ( Symmetric NAT) :这种类型的NAT与上述3种类型的不同,在于当同一内部主机使用相同的端口与不同地址的外部主机进行通信时, NAT对该内部主机的映射会有所不同。对称式NAT不保证所有会话中的私有地址和公开IP之间绑定的一致性。相反,它为每个新的会话分配一个新的端口号。
//
//
// 主要需要对tcp协议属性需要了解学习.
// 当A需要和B建立直接的TCP连接时，首先连接S的【协助打洞】端口，并发送协助连接申请。同时在该端口号上启动侦听。注意由于要在相同的网络终端上绑定到不同的套接字上，所以必须为这些套接字设置 SO_REUSEADDR 属性（即允许重用），否则侦听会失败。

// ----------start----------const----------start----------
var loginfo = log.New(os.Stdout, "[info]:", log.LstdFlags)
var logerr = log.New(os.Stderr, "[err]:", log.LstdFlags)

// ----------end------------const----------end------------
func ParseTcpAddr(addr string) (tcpaddr *net.TCPAddr, err error) {
	return nil, nil
}

// func ParseTcpAddr(addr string) (tcpaddr *net.TCPAddr, err error) {
// 	if strings.TrimSpace(addr) != "" {
// 		if split := strings.Split(addr, ":"); split != nil && len(split) == 2 {
// 			ipstr := split[0]
// 			ipstr2 := strings.Split(ipstr, ".")
// 			// strings.
// 				//
// 				portStr := split[1]
// 			port, _ := strconv.ParseInt(portStr, 10, 0)
// 			tcpaddr := &net.TCPAddr{IP: ipb, Port: int(port)}
//
// 			return tcpaddr, nil
// 		}
// 	}
// 	return nil, errors.New("解析ip失败.不是合法ip地址")
// }

// ip4的地址格式为255.255.255.255，很显然最大值255可以使用一个字节来保存，总共使用4个字节就可以保存，所以使用一个32位的int整型来保存ip地址。
//
// 　　之后从int整形转为ip字符串时，分别对32位的每8位进行处理即可，均可以通过简单的位运算获得

func StringIpToInt(ipstring string) int {
	ipSegs := strings.Split(ipstring, ".")
	var ipInt = 0
	var pos uint = 24
	for _, ipSeg := range ipSegs {
		tempInt, _ := strconv.Atoi(ipSeg)
		tempInt = tempInt << pos
		ipInt = ipInt | tempInt
		pos -= 8
	}
	return ipInt
}

func IntToStringIp2(ipInt int) string {
	ipSegs := make([]string, 4)
	var len = len(ipSegs)
	buffer := bytes.NewBufferString("")
	for i := 0; i < len; i++ {
		tempInt := ipInt & 0xFF
		ipSegs[len-i-1] = strconv.Itoa(tempInt)
		ipInt = ipInt >> 8
	}
	for i := 0; i < len; i++ {
		buffer.WriteString(ipSegs[i])
		if i < len-1 {
			buffer.WriteString(".")
		}
	}
	return buffer.String()
}

func IntToStringIp(ip int) string {
	for x := 1; x <= 4; x++ {
		// tmpint := ip & 255
		loginfo.Printf("IntToStringIp==>二进制字符串%b \n", ip)
		
		tmpint := ip & 0xff
		bitmove := x * 8
		
		asciiInt := strconv.Itoa(tmpint)
		
		loginfo.Printf("%v==>%s \n", x, asciiInt)
		tmpint = tmpint >> uint64(bitmove)
	}
	return ""
}

func TestParseTcpAddr(b testing.B) {
	
}

func tt() {
	
	// net.Listen()
	// listener, e := net.ListenTCP("tcp", )
}
