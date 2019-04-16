/*
--------------------------------------------------
 File Name: tGoroutine.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-16-上午8:51
---------------------说明--------------------------

---------------------------------------------------
*/

package p5_5_concurrent

/*
goroutine 是程序中与其他goroutine 完全相互独立而并发执行的函数或者方法调用。每一个Go 程序都至少有一个goroutine，即会执行main 包中的main()函数的主goroutine。goroutine非常像轻量级的线程或者协程，它们可以被大批量地创建（相比之下，即使是少量的线程也会消耗大量的机器资源）。所有的goroutine共享相同的地址空间，同时Go语言提供了锁原语来保证数据能够安全地跨goroutine共享。然而，Go语言推荐的并发编程方式是通信，而非共享数据。
*/
/*
Go语言的通道是一个双向或者单向的通信管道，它们可用于在两个或者多个goroutine之间通信（即发送和接收）数据。

在goroutine和通道之间，它们提供了一种轻量级（即可扩展的）并发方式，该方式不需要共享内存，因此也不需要锁。但是，与所有其他的并发方式一样，创建并发程序时务必要小心，同时与非并发程序相比，对并发程序的维护也更有挑战。大多数操作系统都能够很好地同时运行多个程序，因此利用好这点可以降低维护的难度。例如，将多份程序（或者相同程序的多份副本）的每一个操作作用于不同的数据上。优秀的程序员只有在其带来的优点明显超过其所带来的负担时才会编写并发程序。
 */

func Main() {
	// 	goroutine使用以下的go语句创建：
	// go function(arguments)
	// go func(parameters) { block } (arguments)
}
