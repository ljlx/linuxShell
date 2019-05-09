/*
--------------------------------------------------
 File Name: test.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-9-下午2:51
---------------------说明--------------------------

---------------------------------------------------
*/

package c2_case_color_Led

import (
	"log"
	"time"
	
	"periph.io/x/periph/conn/gpio"
	"periph.io/x/periph/host"
	"periph.io/x/periph/host/rpi"
	"os"
)

/*
 // Low represents 0v.
    Low Level = false
    // High represents Vin, generally 3.3v or 5v.
    High Level = true
 */

var (
	loginfo = log.New(os.Stdout, "[info]:", log.LstdFlags)
	logerr  = log.New(os.Stderr, "[err]:", log.LstdFlags)
)

func test1() {
	// 加载所有驱动
	if _, err := host.Init(); err != nil {
		log.Fatal(err)
	}
	// ----------start----------我加的测试代码----------start----------
	dutystr := "50%"
	duty, err := gpio.ParseDuty(dutystr)
	if err != nil {
		log.Fatalf("ParseDuty duty fail %v", dutystr)
	}
	if duty.Valid() {
		log.Printf("valu==>DescInfo")
		
	}
	// ----------end------------我加的测试代码----------end------------
	
	ticker := time.NewTicker(500 * time.Millisecond)
	// 针脚11， = bcm283x.GPIO17
	redLed := rpi.P1_11
	
	// 针脚12， = bcm283x.GPIO18
	greenLed := rpi.P1_12
	// l=!l, 对l进行取反赋值, 相当于进行开关的交替进行,聪明.
	for l := gpio.Low; ; l = !l {
		loginfo.Printf("%v==> \n", l)
		
		if err := redLed.Out(l); err != nil {
			log.Fatal(err)
		}
		if err := greenLed.Out(!l); err != nil {
			log.Fatal(err)
		}
		<-ticker.C
	}
}

func test2() {
	led_red := rpi.P1_11   // red gpio-17  ==> P1_11
	led_green := rpi.P1_12 // green gpio-18  ==> P1_12
	led_blue := rpi.P1_32  // blue gpio-12  ==> P1_32
	// 初始化为低电位, 0 ,在这里是false
	curr := gpio.Low
	var (
		err error
	)
	err = led_red.Out(curr)
	err = led_green.Out(curr)
	err = led_blue.Out(curr)
	if err != nil {
		log.Fatalf("%v \n ", err)
	}
	// ----------start----------先开始自检----------start----------
	
	for x := 0; x <= 3; x++ {
		err = led_red.Out(gpio.High)
		err = led_green.Out(gpio.Low)
		err = led_blue.Out(gpio.Low)
		if err != nil {
			log.Fatalf("%v \n ", err)
		}
	}
	loginfo.Printf("质检完成..==> \n")
	
	// ----------end------------先开始自检----------end------------
	
	unitsize := time.Duration(500)
	for {
		//
		loginfo.Printf("test2==>开启红灯 \n")
		err = led_red.Out(gpio.High)
		time.Sleep(time.Millisecond * unitsize)
		//
		loginfo.Printf("test2==>开启绿灯 \n")
		err = led_green.Out(gpio.High)
		time.Sleep(time.Millisecond * unitsize)
		//
		loginfo.Printf("test2==>开启蓝灯 \n")
		err = led_blue.Out(gpio.High)
		time.Sleep(time.Millisecond * unitsize)
		//
		if err != nil {
			log.Fatalf("%v \n ", err)
		}
	}
	
}

func Case2Main() {
	// 加载所有驱动
	// if _, err := host.Init(); err != nil {
	// 	log.Fatal(err)
	// }
	test1()
	test2()
}
