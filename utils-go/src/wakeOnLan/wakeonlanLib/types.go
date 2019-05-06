/*
--------------------------------------------------
 File Name: types.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-5-下午10:09
---------------------说明--------------------------

---------------------------------------------------
*/

package wakeonlanLib





type HumanMac struct {
	/*
	mac的字节表示
	 */
	bMac [6]byte
	/*
	容易可读时,使用的分隔符,如':','-',' '等.
	 */
	humanDivide rune
	/*
	可读字符串
	 */
	humanText string
}

type ProgramArgs struct {
	passwd *string
	logfile *string
	macText []string
}
