/*
--------------------------------------------------
 File Name: c2_case_color_Led.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-9-下午1:14
---------------------说明--------------------------
 双色led
---------------------------------------------------
*/

package c2_case_color_Led

import (
// "github.com/nathan-osman/go-rpigpio"
// "periph.io/x/periph/conn/gpio"
)

var (
	color []int
)

func Main() {
	color = []int{0xFF00, 0x00FF, 0x0FF0, 0xF00F}
	pinsMap := map[string]int{}
	pinsMap["pin_R"] = 11
	pinsMap["pin_R"] = 12
	//
	// pin,_:=rpi.OpenPin(1,1)
	
}
