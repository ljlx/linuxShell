/*
--------------------------------------------------
 File Name: testUnitCase.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-13-下午4:14
---------------------说明--------------------------
 单元测试,执行用例,参考自:https://studygolang.com/articles/12335
---------------------------------------------------
*/

package testUnitCase

func testAdd(m, n int) int {
	return m + n
}

func combination(m, n int) int {
	if n > m-n {
		n = m - n
	}
	
	c := 1
	for i := 0; i < n; i++ {
		c *= m - i
		c /= i + 1
	}
	
	return c
}

func AddAB(a, b int) int {
	return a + b
}
