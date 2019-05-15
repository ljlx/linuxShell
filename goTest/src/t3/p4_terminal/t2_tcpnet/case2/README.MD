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
5. 这里就要