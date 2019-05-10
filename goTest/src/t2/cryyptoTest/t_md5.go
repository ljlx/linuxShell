/*
--------------------------------------------------
 File Name: t_md5.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-10-下午11:13
---------------------说明--------------------------

---------------------------------------------------
*/

package cryyptoTest
import (
"crypto/md5"
"fmt"
"io/ioutil"
)

// TODO 为什么不同平台下 md5结果不一样.
func main() {
md5resu := md5.Sum([]byte("hxadmin1"))
// echo "hxadmin" > /tmp/hx
ss, _ := ioutil.ReadFile("/tmp/hx")
sss := fmt.Sprintf("%x", md5.Sum(ss))
fmt.Printf("linux-md5sum:%v \n", "c78d92b013ee370ffdee7857d61405bb")
fmt.Printf("md5sum-readfile:%v \n", sss)
fmt.Printf("md5-html %v \n", "060c84d2bab4aeebd02a5f1e4978dbe4")
fmt.Printf("md5sum-go: %v \n", fmt.Sprintf("%x", md5resu))

//
mm := md5.New()
bresu := mm.Sum([]byte("hxadmin1"))
fmt.Printf("%v \n", fmt.Sprintf("%x",bresu))
}
