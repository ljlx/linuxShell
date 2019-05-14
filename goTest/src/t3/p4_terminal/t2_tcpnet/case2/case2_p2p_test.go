/*
--------------------------------------------------
 File Name: case2_p2p_test.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-14-下午4:34
---------------------说明--------------------------

---------------------------------------------------
*/

package case2_p2p_test

import (
	"strings"
	"t3/p4_terminal/t2_tcpnet/case2"
	"testing"
)

type IpStr struct {
	ipstr  string
	expect bool
}

var (
	vaildIpList = []IpStr{
		{"10.193.1.1:1234", true},
		{"192.168.1.250:8888", true},
		{"255.255.255.255:1213", true},
		{"0.0.0.0:22", true},
		{"127.0.0.1:22", true},
	}
	
	invaildIpList = []IpStr{
		{"10.193.1.1:65539", false},
		{"10.193.1.1:1111111", false},
		{"10.193.1.1:00", false},
		{"10.1.2.193.1.1:00", false},
		{"10.1.2.193.1.1:00", false},
	}
)

func TestStringIpToInt(t *testing.T) {
	
	var testiplist = append(vaildIpList, invaildIpList...)
	for _, xunit := range testiplist {
		split := strings.Split(xunit.ipstr, ":")
		ipstr := split[0]
		stringIpToInt := case2_p2p.StringIpToInt(ipstr)
		t.Logf("strIp[%v] -> intIp[%v] \n", ipstr, stringIpToInt)
	}
}

func TestIntToStringIp(t *testing.T) {
	var testiplist = append(vaildIpList, invaildIpList...)
	for _, xunit := range testiplist {
		split := strings.Split(xunit.ipstr, ":")
		ipstr := split[0]
		stringIpToInt := case2_p2p.StringIpToInt(ipstr)
		//
		stringIp := case2_p2p.IntToStringIp(stringIpToInt)
		t.Logf("intIp[%v] -> strIp[%v] \n", stringIpToInt, stringIp)
	}
}

func TestParseTcpAddr(t *testing.T) {
	
	var testiplist = append(vaildIpList, invaildIpList...)
	
	for _, xunit := range testiplist {
		tcpaddr, err := case2_p2p.ParseTcpAddr(xunit.ipstr)
		
		case2_p2p.StringIpToInt(xunit.ipstr)
		
		t.Logf("now case %v \n", tcpaddr)
		switch xunit.expect {
		
		case true:
			// err must be nil,tcpaddr should be vaild
			if err != nil {
				t.Errorf("[test] this ipaddr:[%v] is return bug not expect..\n", xunit.ipstr, )
			}
		case false:
			// 	err must be not nil.
			if err == nil {
				t.Errorf("[test] this case must be fail,the expect is false,but err is nil.the value is %v \n", xunit.ipstr)
			}
		}
	}
}
