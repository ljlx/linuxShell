/*
--------------------------------------------------
 File Name: interfaces.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-10-下午9:12
---------------------说明--------------------------
 接口抽象集合
---------------------------------------------------
*/

package main

type MoneyHandler interface {
	/*
	handler名称
	 */
	name() (string)
	/*
	不同money优惠计算方法
	 */
	handle(a, b int) (result int, err error)
	
	/*
	是否支持此数据范围
	 */
	supper(a, b int) (isSupport bool)
}

type SortHandler interface {
	/*
	使用嵌入的方法,类似与java的接口继承.
	 */
	MoneyHandler
	/*
	得到排序值
	 */
	GetSort() (sort int)
}

type HookHandler interface {
	MoneyHandler
	/*
	接口注册hook,抽象层次调用callback.
	 */
	GetHookCallBack() (func(a, b int) (a1, m1 int))
}

