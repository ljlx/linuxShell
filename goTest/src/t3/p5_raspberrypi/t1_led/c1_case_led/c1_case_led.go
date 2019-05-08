/*
--------------------------------------------------
 File Name: c1_case_led.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-8-下午10:29
---------------------说明--------------------------
 树莓派3b+ 点亮led小灯.
---------------------------------------------------
*/

package c1_case_led

import (
	"bufio"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
	"time"
	
	"github.com/nathan-osman/go-rpigpio"
)

var (
	loginfo = log.New(os.Stdout, "info=>", log.LstdFlags)
	logerr  = log.New(os.Stderr, "error=>", log.LstdFlags)
)

/*
 关于linux操作GPIO的说明,参考 https://blog.csdn.net/lu_embedded/article/details/53061901
 */
func Main() {
	os.Args = append(os.Args, "2")
	
	if len(os.Args) < 2 {
		logerr.Fatalf("usage %v [0-40]", os.Args[0])
	}
	arg2 := os.Args[1]
	pinnums, err := strconv.ParseInt(arg2, 0, 0)
	//
	reader := bufio.NewReader(os.Stdin)
	goon := true
	for goon {
		loginfo.Printf("你输入的是%v,确定要向此pin口发送闪烁消息吗:yes or no ? :", arg2)
		line, _, err := reader.ReadLine()
		if err != nil {
			if err == io.EOF {
				line=[]byte("yes")
			}else {
				log.Fatalf("%v", err)
			}
		}
		b := strings.ToLower(string(line))
		
		switch b {
		case "yes":
			loginfo.Println("yes:", b)
			goon = false
			break
		case "no":
			loginfo.Println("no:", b)
			return
		}
	}
	loginfo.Printf("开始向pin口{%v} 发生闪烁消息...", arg2)
	//
	pin, err := rpi.OpenPin(int(pinnums), rpi.OUT)
	
	if err != nil {
		log.Fatalf("openpin 失败... %v,%v. err msg:%v", 2, rpi.OUT, err)
	}
	defer pin.Close()
	
	// set high 设置高电位,相当于二进制的1.
	// LOW  = iota // pin is low (off)
	// HIGH        // pin is high (on)
	pin.Write(rpi.HIGH)
	loginfo.Printf("start gpio test...")
	go func() {
		for true {
			time.Sleep(time.Millisecond * 500)
			pin.Write(rpi.HIGH)
			loginfo.Printf("on. \n")
			//
			time.Sleep(time.Millisecond * 500)
			pin.Write(rpi.LOW)
			loginfo.Printf("off. \n")
		}
	}()
	time.Sleep(time.Minute)
	
}
