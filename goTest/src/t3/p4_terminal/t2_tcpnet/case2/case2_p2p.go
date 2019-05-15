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
	"fmt"
	"log"
	"net"
	"os"
	"strconv"
	"strings"
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
	ipport := strings.Split(addr, ":")
	// ip
	intip := StringIpToInt(ipport[0])
	ip1 := byte((intip >> 24) & 0xff)
	ip2 := byte((intip >> 16) & 0xff)
	ip3 := byte((intip >> 8) & 0xff)
	ip4 := byte((intip) & 0xff)
	// port
	port, err := strconv.ParseInt(ipport[1], 10, 16)
	tcpaddr = &net.TCPAddr{IP: []byte{ip1, ip2, ip3, ip4}, Port: int(port)}
	return tcpaddr, nil
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

/*
	4字节int,转化为数字符常用ip形式.
比如: 180420864 -> 10.193.1.1

*/
func IntToStringIp(ip int) string {
	ip1 := (ip >> 24) & 0xff
	ip2 := (ip >> 16) & 0xff
	ip3 := (ip >> 8) & 0xff
	ip4 := ip & 0xff
	return fmt.Sprintf("%d.%d.%d.%d", ip1, ip2, ip3, ip4)
}

func IntToStringIpDebug(ip int) string {
	// 以下提到的范围[x~x],表示的是10进制数字的范围.
	//
	// 1. 由于int是4个字节组成的.而ip由每一个'.'号分割的每一个数字范围是[0-255],是由无符号的一个字节(无符号一个字节大小范围是[0-255])组成.(有符号的一个字节所能表示的值是[-127~127] ).
	// 2. 所以每一个'.'号分割的数字由一个字节8位表示即二进制表示法,范围[00000000~11111111]
	// 3. 假如有一个ip: 10.193.1.1,其二进制表示:00001010,11000001,00000001,00000001. 转化为10进制数字为:180420864
	// 4. 求ip2:将上述二进制符往右边移动16位,结果:00000000,00000000,00001010,11000001.
	// 5. 16进制数字0xff,代表一个字节的全是1位,即 11111111.
	// 6. 进行与运算.'&' 按照字节的每一位,进行与运算:0&0=0, 1&0=0, 0&1=0 ,1&1=1
	// 7. 因此将ip2移位后(步骤4)和0xff(步骤5) 进行与运算 ,计算出结果为:00000000,00000000,00000000,11000001. 转成可读10进制数字为: 193
	//
	// 具体二进制移位效果和10进制数字.可以使用 程序员计算器app来方便计算得到结果,帮助理解.
	ip1 := (ip >> 24) & 0xff
	// ip11 := (ip >> 24)
	ip2 := (ip >> 16) & 0xff
	// ip22 := (ip >> 24)
	ip3 := (ip >> 8) & 0xff
	// ip33 := (ip >> 8)
	ip4 := ip & 0xff
	// print(ip11, ip22, ip33)
	return fmt.Sprintf("%d.%d.%d.%d", ip1, ip2, ip3, ip4)
	
	// for x := 1; x <= 4; x++ {
	// 	// tmpint := ip & 255
	// 	loginfo.Printf("IntToStringIp==>二进制字符串%b \n", ip)
	//
	// 	tmpint := ip & 0xff
	// 	bitmove := 8
	//
	// 	asciiInt := strconv.Itoa(tmpint)
	//
	// 	loginfo.Printf("%v==>%s \n", x, asciiInt)
	// 	ip = ip >> uint64(bitmove)
	// }
	// return ""
}

func testp2p() (err error) {
	
	// tcpaddr, _ := ParseTcpAddr("0.0.0.0:44444")
	// listener, err := net.ListenTCP("tcp", tcpaddr)
	// conn, err := net.DialIP("", nil, nil)
	// conn.
	
}
