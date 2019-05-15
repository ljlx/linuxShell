/*
--------------------------------------------------
 File Name: macparser.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-15-下午7:09
---------------------说明--------------------------
 快速将常用的mac地址信息转换输出.
---------------------------------------------------
*/

package macparser

import (
	errors2 "errors"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
	
	"golang.org/x/crypto/openpgp/errors"
)

// D0509996526F
// D0:50:99:96:52:6F
// D0-50-99-96-52-6F
// 1. mac单个表示点最高16进制表示为FF
// 2. 16进制FF换成2进制是 1111 1111 刚好8位即一个字节
// 所以可以用6个字节来表示一个mac地址.

var (
	supportList []string = []string{":", "-", " ", ""}
	registerMap          = make(map[string]func(macaddr string) (macobj *Tmacaddr, err error))
	
	// ParserSupport1 = Parser(":")
	// ParserSupport2 = Parser("-")
	// ParserSupport3 = Parser(" ")

)

func init() {
	
	for index, _ := range supportList {
		key := supportList[index]
		parser := macParser(key)
		registerMap[key] = parser
	}
	
}

type Tmacaddr struct {
	Inputmac    string
	macstr      []string
	macbyte     []uint8
	macnum      uint64
	formatSplit string
	vaild       bool
}

var loginfo = log.New(os.Stdout, "[info]:", log.LstdFlags)
var logerr = log.New(os.Stderr, "[err]:", log.LstdFlags)

// ----------start----------type Tmacaddr method----------start----------

func (mac *Tmacaddr) support(splitChar string) bool {
	// && strings.ContainsRune(mac.Inputmac,splitChar)
	return mac.Inputmac != "" && strings.Count(mac.Inputmac, splitChar) == 5
}

/*
自动从支持的分隔符列表(":", "-", " ", "")中进行自动解析.
*/
func (mac *Tmacaddr) MParserMacAddress() error {
	
	if mac.Inputmac != "" {
		for index, _ := range supportList {
			splitchar := supportList[index]
			if mac.support(splitchar) {
				parserFunc := registerMap[splitchar]
				macobj, err := parserFunc(mac.Inputmac)
				if err != nil {
					logerr.Printf("parserFunc %v \n ", err)
					return err
				}
				err = macobj.MFillMacObj()
				mac.formatSplit = splitchar
				mac.macbyte = macobj.macbyte
				mac.macnum = macobj.macnum
				mac.macstr = macobj.macstr
				return err
			}
			
		}
		
	}
	
	unsupportedError := errors.UnsupportedError(fmt.Sprintf("the mac address is invaild.%v", mac.Inputmac))
	return errors2.New(string(unsupportedError))
}

func (mac *Tmacaddr) MFillMacObj() (err error) {
	macaddr := mac.Inputmac
	loginfo.Printf("mac转换==>MAC地址:%v \n", macaddr)
	macchar := mac.macstr
	var macnum uint64 = 0
	mac.macbyte = make([]byte, 6, 6)
	for index, _ := range macchar {
		// macint, err := strconv.Atoi(macchar[index])
		u := macchar[index]
		// 把16进制的mac字符转化为10进制数字
		parseUint, err := strconv.ParseUint(string(u), 16, 8)
		mac.macbyte[index] = uint8(parseUint)
		if err != nil {
			return err
		}
		// 	向一个8个字节大小(64bit)的int64类型存放mac值.
		moveBit := (6 - index) << 3
		tmpint := parseUint << uint8(moveBit)
		macnum = macnum | tmpint
		loginfo.Printf("mac转换==>16进制字符:%v,10进制数字:%v,左移%v位存储数字:%v,二进制当前字符:%v,汇总字符%v \n", u, parseUint, moveBit, macnum, fmt.Sprintf("%b", parseUint), fmt.Sprintf("%b", macnum))
		
	}
	mac.macnum = macnum
	return nil
}

func (mac *Tmacaddr) VaildMacNum() {
	nummac := mac.macnum
	u1 := nummac >> (6 << 3) & 0xff
	u2 := nummac >> (5 << 3) & 0xff
	u3 := nummac >> (4 << 3) & 0xff
	u4 := nummac >> (3 << 3) & 0xff
	u5 := nummac >> (2 << 3) & 0xff
	u6 := nummac >> (1 << 3) & 0xff
	loginfo.Printf("%v-%v-%v-%v-%v-%v==> \n", u1, u2, u3, u4, u5, u6)
	// TODO 位数不足要补齐.应用fmt语法.
	loginfo.Printf("%x-%x-%x-%x-%x-%v==> \n", u1, u2, u3, u4, u5, u6)
	
}

// ----------end------------type Tmacaddr method----------end------------

func macParser(splitchar string) func(macaddr string) (macobj *Tmacaddr, err error) {
	
	return func(macaddr string) (macobj *Tmacaddr, err error) {
		macchar := strings.Split(macaddr, splitchar)
		macobj = new(Tmacaddr)
		macobj.Inputmac = macaddr
		macobj.macstr = macchar
		//
		return macobj, nil
		
	}
}
