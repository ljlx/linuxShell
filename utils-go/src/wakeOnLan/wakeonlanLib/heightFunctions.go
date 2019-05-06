/*
--------------------------------------------------
 File Name: heightFunctions.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-5-下午11:27
---------------------说明--------------------------
 高阶函数定义
---------------------------------------------------
*/

package wakeonlanLib

/*
TODO 假泛型如何使用?
 */
func HFmap(emums []string, mapfunc func(string) (string)) {
	for index, _ := range emums {
		emums[index] = mapfunc(emums[index])
	}
	return
}
