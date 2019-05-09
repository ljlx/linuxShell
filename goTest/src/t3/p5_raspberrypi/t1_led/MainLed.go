/*
--------------------------------------------------
 File Name: MainLed.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-8-下午10:30
---------------------说明--------------------------
 main
---------------------------------------------------
*/

package main

import (
	// "t3/p5_raspberrypi/t1_led/c1_case_led"
	
	"t3/p5_raspberrypi/t1_led/c2_case_color_Led"
)

func main() {
	// c1_case_led.Main()
	c2_case_color_Led.Case2Main()
}