/*
--------------------------------------------------
 File Name: wakeOnLan.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-5-下午9:45
---------------------说明--------------------------
 wake on lan
---------------------------------------------------
*/

package wakeonlanLib

import (
	"flag"
	"log"
	"os"
	"strings"
)

// D0509996526F
// D0:50:99:96:52:6F
// D0-50-99-96-52-6F
// 1. mac单个表示点最高16进制表示为FF
// 2. 16进制FF换成2进制是 1111 1111 刚好8位即一个字节
// 所以可以用6个字节来表示一个mac地址.

/*
帮助信息.
 */
func usageInfo() {
	programName := os.Args[0]
	log.Fatalf("usage: %v [-p passwd] macaddr", programName)
}

func parseArgs() (args *ProgramArgs, err error) {
	programArgs := new(ProgramArgs)
	
	programArgs.passwd = flag.String("p", "", "passwd")
	programArgs.logfile = flag.String("o", "", "logfile")
	
	flag.Parse()
	programArgs.macText = flag.Args()
	// 处理mac地址切片
	
	return programArgs, nil
}

func Main() {
	var (
		progremArgs *ProgramArgs
		err         error
	)
	if progremArgs, err = parseArgs(); err != nil {
		log.Fatalf("parse args has been error ,%v", err)
	}
	
	// use to mac
	HFmap(progremArgs.macText, func(s string) string {
		return strings.TrimSpace(s)
	})
	
	
}
