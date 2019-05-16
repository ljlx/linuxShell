#### 心得
> 参考博文:   
    1. [P2P技术基础: 关于TCP打洞技术](https://www.cnblogs.com/snowbook/p/5133278.html)  
    2. [P2P技术基础: UDP打洞原理](https://blog.csdn.net/D_R_L_T/article/details/81196101)  
    3. [golang实现p2p之UDP打洞](https://blog.csdn.net/qq_31967569/article/details/82704340)  

经过对[p2p理论](https://www.cnblogs.com/snowbook/p/5133278.html)的学习. 我使用终端来尝试打洞,并且打洞成功了.传输速度很快. 具体速度根据运营商带宽的情况来看 最快有3m 左右的速度了.


具体操作步骤如下(纯手动的,也是最简单): 

1. 先在服务端(hk.thesunboy.com),启动了一个进程,该进程的作用是监听一个端口比如说 8088,服务段程序唯一的功能是向客户端输出客户端连接的外网ip和端口
    ```
        [user@server]$  ./TestMain
        [info]:2019/05/14 15:04:50 ServerListener==> 开启服务器成功 
        [err]:2019/05/14 15:05:02 accept==>建立连接8088成功... 
        [info]:2019/05/14 15:05:02 serverTest协程==> func(*terminal.Terminal) 
        [info]:2019/05/14 15:05:02 ==> func() 
    ```
2.  客户端(local:192.168.0.51) 使用telnet程序向服务端(hk.thesunboy.com) ,这时候服务器返回了我当前客户端所在的外网ip和端口,如 113.246.87.125:7173
    ```
    [user@client]$ telnet hk.thesunboy.com 8088
                   Trying 47.52.94.171...
                   Connected to hk.thesunboy.com.
                   Escape character is '^]'.
                   hello. you ip:113.246.87.125:7173
    
    ```
  
3. 这个时候可以在客户端通过命令 ``` netstat ``` 查看当前的连接的状况.由输出结果可知,我们此次通过了本地地址``` 192.168.0.51:38726 ``` 和远程外网服务器地址 ``` 47.52.94.171:8088 ``` 建立了一个连接. 连接的状态是: ESTABLISHED 代表连接已建立.这个时候代表者,客户端在客户端的外网ip(113.246.87.125) 打了个洞,其在NET网关设备上的端口号是7173,绑定的内网客户端端口是38726
    ```
    [user@client]$ netstat -np|grep telnet
        （并非所有进程都能被检测到，所有非本用户的进程信息将不会显示，如果想看到所有信息，则必须切换到 root 用户）
         tcp        0      0 192.168.0.51:38726      47.52.94.171:8088       ESTABLISHED 11004/telnet
    ```
4.  我在telnet中随便输入了点内容发到服务器去,服务端也正确的给我响应了.证明连接状态是可以相互通信的.
    接着我把客户端与服务器的连接在中断退出了.但是由于我没有发送 终止信号. 所以再次查询链接的时候,状态显示为: ``` FIN_WAIT1 ``` ,这个时候 我如果选择在客户端侦听这个端口38726,会报端口已被占用的错误,大概是因为需要开启Socket的 ```  SO_REUSEADDR ```端口复用属性吧.
    ```
    [user@client]$ telnet hk.thesunboy.com 8088  
    Trying 47.52.94.171...  
    Connected to hk.thesunboy.com.  
    Escape character is '^]'.  
    hello. you ip:113.246.87.125:7173
    >hi,server
    hi,server
    you resp:hi,server
    >
    
    [user@client]$ netstat -np|grep 192.168.0.51:38726
    （并非所有进程都能被检测到，所有非本用户的进程信息将不会显示，如果想看到所有信息，则必须切换到 root 用户）
    tcp        0      1 192.168.0.51:38726      47.52.94.171:8088       FIN_WAIT1   -
    
    [user@client]$ python3 -m http.server 38726
    Traceback (most recent call last):
      File "/home/hanxu/anaconda3/lib/python3.6/runpy.py", line 193, in _run_module_as_main
        "__main__", mod_spec)
      ......
        socketserver.TCPServer.server_bind(self)
      File "/home/hanxu/anaconda3/lib/python3.6/socketserver.py", line 470, in server_bind
        self.socket.bind(self.server_address)
        
    OSError: [Errno 98] Address already in use
    ```
5. 这个时候我把服务端的进程关掉(/lb可能是因为我服务端没有及时销毁客户端断开的链接吧.),在不断的重复尝试查看连接的状态 ```netstat -np|grep 192.168.0.51:38726```,直到我发现这条连接消失了.我就趁着Net网关还没及时销毁这个内网端口到外网Nat设备的映射信息, 赶紧使用 ``` python3 -m http.server 38726 ``` 来监听住这个内网端口,并且尝试在外网 ``` curl  113.246.87.125:7173 ``` 这个地址,如果这次p2p打洞成功,那么curl 会输出我本地python服务器的响应.
    ```
    [user@server]$  curl -v 113.246.87.125:7173
    *   Trying 113.246.87.125...
    * TCP_NODELAY set
    * Connected to 113.246.87.125 (113.246.87.125) port 7173 (#0)
    > GET / HTTP/1.1
    > Host: 113.246.87.125:7173
    > User-Agent: curl/7.63.0
    > Accept: */*
    >
    * HTTP 1.0, assume close after body
    < HTTP/1.0 200 OK
    < Server: SimpleHTTP/0.6 Python/3.6.8
    < Date: Thu, 16 May 2019 01:29:06 GMT
    < Content-type: text/html; charset=utf-8
    < Content-Length: 553
    <
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Directory listing for /</title>
    ......
    </body>
    </html>
    * Closing connection 0

    ```
   如果不幸失败的话,无法连接到这个地址```  113.246.87.125:7173 ```, 就要重复上述的整个过程.
 ---
 6. 
 
 > 总结: 这个过程虽然粗糙简单,而且涉及到tcp协议的相关知识,但是也足以窥见流程是能打通的.能够用代码去实现.
 从中也明白, 自己对网络相关的知识欠缺, 不了解tcp的各种状态和属性.需要加强提高啊.