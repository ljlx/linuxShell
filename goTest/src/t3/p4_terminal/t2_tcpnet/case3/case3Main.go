/*
--------------------------------------------------
 File Name: case3Main.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-16-下午4:47
---------------------说明--------------------------

---------------------------------------------------
*/

package case3_p2p

import (
	"os"
)

func Main() {
	s := os.Args[1]
	// unix 管道编程.
	// r, w, err := os.Pipe()
	
	loginfo.Printf("启动==>%v \n", s)
	switch s {
	case "server":
		loginfo.Printf("选择启动==>%v \n", s)
		
		Mainp2pServer()
	case "client":
		tagname := os.Args[2]
		loginfo.Printf("选择启动==>%v \n", s)
		Mainp2pClient(tagname)
	}
	
}
