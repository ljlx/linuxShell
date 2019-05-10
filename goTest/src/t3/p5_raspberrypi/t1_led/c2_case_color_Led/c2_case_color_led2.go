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
	"os/signal"
	"reflect"
	"syscall"
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
	// dutystr := "50%"
	// duty, err := gpio.ParseDuty(dutystr)
	// if err != nil {
	// 	log.Fatalf("ParseDuty duty fail %v", dutystr)
	// }
	// if duty.Valid() {
	// 	log.Printf("valu==>DescInfo")
	//
	// }
	// ----------end------------我加的测试代码----------end------------
	
	ticker := time.NewTicker(500 * time.Millisecond)
	// 针脚11， = bcm283x.GPIO17
	// 参考树莓派40pin引脚对照表.
	// 物理引脚 board编码 为11的, 对应 bcm编码为17.
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

type Led_rgb struct {
	led_red   gpio.PinIO "red for rgb led"
	led_green gpio.PinIO "green for rgb led"
	led_blue  gpio.PinIO "blue for rgb led"
}

func (led *Led_rgb) CleanLed() {
	// loginfo.Printf("cleanled==>start... \n")
	led.led_red.Out(gpio.Low)
	led.led_green.Out(gpio.Low)
	led.led_blue.Out(gpio.Low)
	// loginfo.Printf("cleanled==>end... \n")
}
func (led *Led_rgb) getRGB() ([]gpio.PinIO) {
	leds := []gpio.PinIO{led.led_red, led.led_green, led.led_blue}
	return leds
}

func (led *Led_rgb) FlashAll(timesec time.Duration) (err error) {
	
	leds := led.getRGB()
	for {
		for index := range leds {
			leditem := leds[index]
			err = leditem.Out(gpio.High)
			time.Sleep(time.Millisecond * timesec)
			led.CleanLed()
			//
			if err != nil {
				log.Fatalf("%v \n ", err)
			}
		}
	}
	return nil
}

/*
我的灯大,我的灯亮,我的灯还会闪...
 */
func (led *Led_rgb) Flash(index int, count int) (err error) {
	leds := led.getRGB()
	ledx := leds[index]
	loginfo.Printf("Flash==>我的灯大,我的灯亮,我的灯还会闪...%v \n", index)
	
	ledx.Out(gpio.Low)
	for x := 0; x < count; x++ {
		loginfo.Printf("Flash==>灯亮[%v] \n", x)
		err = ledx.Out(gpio.High)
		time.Sleep(time.Millisecond * 50)
		err = ledx.Out(gpio.Low)
		time.Sleep(time.Millisecond * 50)
		loginfo.Printf("Flash==>灯灭 %v\n", err)
		
	}
	return nil
}

func exitSignal(ledrgb *Led_rgb) {
	// 按照系统api定义接收系统退出信号队列.
	c := make(chan os.Signal)
	// 向程序注册hook.,当程序收到信号要退出时,会向注册的hook发起事件消息.应该只适用于非-9退出吧
	signal.Notify(c, syscall.SIGINT, syscall.SIGSTOP, syscall.SIGTERM, syscall.SIGKILL, syscall.SIGABRT)
	
	for {
		// 从信号队列取出信号信息对象值
		s := <-c
		logerr.Printf("testled==>get signal %v  \n", s)
		signalname := s.String()
		signalType := reflect.TypeOf(s)
		signalure := s.Signal
		loginfo.Printf("信号信息:{name:%v,type:%v,signalure:%v}==> \n", signalname, signalType, signalure)
		s.Signal()
		// if  {
		loginfo.Printf("准备结束程序啦begin...")
		ledrgb.CleanLed()
		loginfo.Printf("准备结束程序啦end...")
		os.Exit(0)
		// } else {
		// 	loginfo.Printf("信号不再结束列表里%v, %d==> \n", s)
		// 0 1 2
		// 3-0=3 ,3-1=2,3-3=0,
		// }
		
	}
}

func test2() {
	
	led_red := rpi.P1_11   // red gpio-17  ==> P1_11
	led_green := rpi.P1_12 // green gpio-18  ==> P1_12
	led_blue := rpi.P1_29  // blue gpio-5  ==> P1_29
	ledrgb := &Led_rgb{led_red, led_green, led_blue}
	// 初始化为低电位, 0 ,在这里是false
	
	var (
		err error
	)
	defer func() {
		err2 := recover()
		if err2 != nil {
			log.Fatalf("errmesg :%v \n ", err2)
		}
	}()
	//
	go test1()
	
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
	ledrgb.CleanLed()
	os.Exit(1)
	
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

func test3() {
	led := &Led_rgb{rpi.P1_11, rpi.P1_12, rpi.P1_32}
	led.CleanLed()
	led.Flash(0, 3)
	led.Flash(1, 3)
	led.Flash(2, 3)
	//
	loginfo.Printf("test3==>交替闪.. \n")
	
	leds := led.getRGB()
	go func() {
		for {
			for x := range leds {
				led.Flash(x, 1)
				// leds[x].Out(gpio.High)
				// time.Sleep(time.Millisecond * 150)
				// leds[x].Out(gpio.Low)
			}
		}
	}()
	//
	
	// led.FlashAll(200)
	// led.CleanLed()
	exitSignal(led)
}

func Case2Main() {
	// 加载所有驱动
	if _, err := host.Init(); err != nil {
		log.Fatal(err)
	} //
	// test1()
	// test2()
	test3()
}
