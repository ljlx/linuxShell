/*
--------------------------------------------------
 File Name: macparser_test.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-15-下午8:03
---------------------说明--------------------------
 test for macparser
---------------------------------------------------
*/

package macparser_test

import (
	"testing"
	
	"macparser"
)

func getRightMacAddress() ([]testMacaddress) {
	
	return []testMacaddress{
		{"00:16:3e:00:17:39", true},
		{"2c:b0:5d:f3:02:a6", true},
		
		{"02:42:38:f0:b3:2b", true},{"2c:b0:5d:f3:02:a6", true},
		
	}
}

type testMacaddress struct {
	macaddr string
	except  bool
}

func TestParser(t *testing.T) {
	for _, x := range getRightMacAddress() {
		tmacaddr := new(macparser.Tmacaddr)
		tmacaddr.Inputmac=x.macaddr
		// macobj, err := tmacaddr.MParserMacAddress()
		err := tmacaddr.MParserMacAddress()
		// tmacaddr.MFillMacObj()
		tmacaddr.VaildMacNum()
		switch x.except {
		case true:
			if err != nil {
				t.Errorf("macaddr:%v is except vaild, but this test case has been err : %v \n", x.macaddr, err)
			}
		case false:
			if err == nil {
				t.Errorf("macaddr:%v is invaild, but it is not return err. value:%v \n", x.macaddr,tmacaddr)
			}
		}
		
	}
	
}
