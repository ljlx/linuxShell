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

import (
	"fmt"
)

/*
goroutine 是程序中与其他goroutine 完全相互独立而并发执行的函数或者方法调用。每一个Go 程序都至少有一个goroutine，即会执行main 包中的main()函数的主goroutine。goroutine非常像轻量级的线程或者协程，它们可以被大批量地创建（相比之下，即使是少量的线程也会消耗大量的机器资源）。所有的goroutine共享相同的地址空间，同时Go语言提供了锁原语来保证数据能够安全地跨goroutine共享。然而，Go语言推荐的并发编程方式是通信，而非共享数据。
*/
/*
Go语言的通道是一个双向或者单向的通信管道，它们可用于在两个或者多个goroutine之间通信（即发送和接收）数据。

在goroutine和通道之间，它们提供了一种轻量级（即可扩展的）并发方式，该方式不需要共享内存，因此也不需要锁。但是，与所有其他的并发方式一样，创建并发程序时务必要小心，同时与非并发程序相比，对并发程序的维护也更有挑战。大多数操作系统都能够很好地同时运行多个程序，因此利用好这点可以降低维护的难度。例如，将多份程序（或者相同程序的多份副本）的每一个操作作用于不同的数据上。优秀的程序员只有在其带来的优点明显超过其所带来的负担时才会编写并发程序。
 */

func case1_channel() {
	// 	少数情况下需要开启一串的goroutine，并等待它们完成，同时也不需要通信。然而，在大多数情况下，goroutine之间需要相互协作，这最好通过让它们相互通信来完成。下面是用于发送和接收数据的语法：
	// channel <- value　　　　　 // 阻塞发送
	// <-channel　　　　　　　　　// 接收并将其丢弃
	// x := <-channel　　　　　　 // 接收并将其保存
	// x, ok := <-channel　　　　 // 功能同上，同时检查通道是否已关闭或者是否为空
	// 非阻塞的发送可以使用select语句来达到，或者在一些情况下使用带缓冲的通道。通道可以使用内置的make()函数通过以下语法来创建：
	// make(chan Type)
	// make(chan Type, capacity)
	// 	如果没有声明缓冲区容量，那么该通道就是同步的，因此会阻塞直到发送者准备好发送和接收者准备好接收。如果给定了一个缓冲区容量，通道就是异步的。只要缓冲区有未使用空间用于发送数据，或还包含可以接收的数据，那么其通信就会无阻塞地进行。
	
	// 通道默认是双向的,但如果需要我们可以使得它们是单向的。例如，为了以编译器强制的方式更好地表达我们的语义。在第7章中我们将看到如何创建单向的通道，然后在任何适当的时候都使用单向通道。
	counterA := case1_channel_make(0, 5)
	counterB := case1_channel_make(0, 78)
	fmt.Printf("通道创建完毕...\n")
	for i := 0; i < 5; i++ {
		// 	通道中接收一个数据
		a := <-counterA
		// 第一种接收方式将获取的数据保存到一个变量里，第二种接收方式将接收的值直接以参数的形式传递给一个函数。
		fmt.Printf("从通道中获取一个数字: a <- conterA ,a=%d \n", a)
		fmt.Printf("(A→%d, B→%d) \n", a, <-counterB)
	}
	
	// ----------start----------test----------start----------
	// TODO 为什么这段go协程没有执行?
	binloop := make(chan int, 2)
	go func() {
		fmt.Printf("dead line loop")
		for {
			binloop <- 1
			fmt.Printf("%d", <-binloop)
			
		}
	}()
	fmt.Printf("lalala")
	// ----------end------------test----------end------------
}

func case1_channel_make(bufsize, start int) (chan int) {
	// xIntchan := make(chan int, bufsize)
	xIntchanNext := make(chan int)
	go func(start int) {
		for {
			// 如果xIntchanNext通道里的内容没有被消费掉,在循环中再次push会阻塞住.
			// 应该和队列差不多,不过通道是双向队列.语言层面上的.
			fmt.Printf("goroutine语句执行[%d]...\n", start)
			xIntchanNext <- start
			start++
		}
	}(start)
	return xIntchanNext
}

func Main() {
	fmt.Printf("通道和goroutine测试...start...\n")
	// 	goroutine使用以下的go语句创建：
	// go function(arguments)
	// go func(parameters) { block } (arguments)
	case1_channel()
	fmt.Printf("通道和goroutine测试...end...\n")
}
