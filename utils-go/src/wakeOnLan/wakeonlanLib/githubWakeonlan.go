/*
--------------------------------------------------
 File Name: githubWakeonlan.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-5-下午11:52
---------------------说明--------------------------
 来自 https://github.com/ymotongpoo/wakeonlan
---------------------------------------------------
*/


package wakeonlanLib

import (
	"bytes"
	"flag"
	"fmt"
	"log"
	"net"
	"strconv"
	"strings"
)



type MagicPacket struct {
	Sync      []byte
	TargetMAC []byte
	Password  []byte
}

func stringToAddr(macStr string) ([]byte, error) {
	trimed := strings.TrimSpace(strings.Replace(macStr, ":", "", -1))
	if len(trimed) != 12 {
		return nil, fmt.Errorf("unsupported MAC address: %v", macStr)
	}
	buf := make([]byte, 6)
	for i := 0; i < 6; i++ {
		n, err := strconv.ParseInt(trimed[2*i:2*(i+1)], 16, 10)
		if err != nil {
			return nil, err
		}
		buf[i] = byte(n)
	}
	return buf, nil
}

func NewMagicPacket(mac string, pass []byte) (*MagicPacket, error) {
	buf, err := stringToAddr(mac)
	if err != nil {
		return nil, err
	}
	targetMAC := make([]byte, 96)
	for i := 0; i < 16; i++ {
		copy(targetMAC[6*i:6*(i+1)], buf)
	}
	return &MagicPacket{
		Sync:      []byte{0xff, 0xff, 0xff, 0xff, 0xff, 0xff},
		TargetMAC: targetMAC,
		Password:  pass,
	}, nil
}

func (p *MagicPacket) TargetMACAddr() string {
	if len(p.TargetMAC) != 96 {
		return "unknown address"
	}
	return string(p.TargetMAC[0:6])
}

func (p *MagicPacket) Broadcast() error {
	conn, err := net.Dial("udp", "255.255.255.255:9")
	if err != nil {
		return err
	}
	buf := new(bytes.Buffer)
	buf.Write(p.Sync)
	buf.Write(p.TargetMAC)
	buf.Write(p.Password)
	_, err = conn.Write(buf.Bytes())
	return err
}

// ----------------example-----------------


var pass = flag.String("p", "", "password string")

func usage() {
	fmt.Println("usage: wol [-p password] macaddr")
}

func GithubMain() {
	flag.Parse()
	
	if flag.NArg() < 1 {
		usage()
	}
	
	mac := strings.TrimSpace(flag.Arg(0))
	p, err := NewMagicPacket(mac, []byte(*pass))
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Sending Magic Packet to %v\n", mac)
	err = p.Broadcast()
	if err != nil {
		log.Fatal(err)
	}
}