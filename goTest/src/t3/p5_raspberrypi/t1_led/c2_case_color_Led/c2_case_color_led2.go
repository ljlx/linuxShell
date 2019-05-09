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
)

func Case2Main() {
	// 加载所有驱动
	if _, err := host.Init(); err != nil {
		log.Fatal(err)
	}
	
	ticker := time.NewTicker(500 * time.Millisecond)
	// 针脚11， = bcm283x.GPIO17
	redLed := rpi.P1_11
	// 针脚12， = bcm283x.GPIO18
	greenLed := rpi.P1_12
	for l := gpio.Low; ; l = !l {
		if err := redLed.Out(l); err != nil {
			log.Fatal(err)
		}
		if err := greenLed.Out(!l); err != nil {
			log.Fatal(err)
		}
		<-ticker.C
	}
}
