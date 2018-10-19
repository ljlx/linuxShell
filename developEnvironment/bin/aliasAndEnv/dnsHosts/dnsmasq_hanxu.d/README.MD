dnsmasq是一个小巧且方便地用于配置DNS和DHCP的工具，适用于小型网络，相比bind和dhcpd，配置起来更简单。dnsmasq能够提供本地解析和外部dns服务器代理，通常将将其作为一个DNS中继代理。openstack就是采用的dnsmasq。



1、dnsmasq安装

yum -y install dnsmasq 
安装完成之后可以通过”dnsmasq –help” 或 “man 8 dnsmasq”查看支持的配置详情。

2、配置dnsmasq

配置都在一个文件中完成/etc/dnsmasq.conf。默认情况下dnsmasq.conf中只开启了最后include项，可以在/etc/dnsmasq.d中自己写任意名字的配置文件。 
vi /etc/dnsmasq.conf



#监听的端口，dns默认53端口,如果设置为0，则完全禁止DNS功能
port=53
#监听地址
listen-address=192.168.145.134

#正确的域名格式才转发
domain-needed

#设置本地域扩展，相当于域简写，如hosts配置 www 会自动加上www.zhutw.com
expand-hosts
local=/zhutw.com/

#配置上游的nameserver解析文件
#resolv-file=/etc/dnsmasq.resolv.conf
#当/etc/resolv.conf或resolv-file文件变化，不重新加载
no-poll
#不使用上游nameserver配置文件(/etc/resolv.conf和resolv-file）
no-resolv

#配置本地解析的hosts
addn-hosts=/etc/dnsmasq.hosts
#不使用/etc/hosts，开启后expand-hosts不生效
#no-hosts

#按配置顺序查询上级nameserver服务器
strict-order

#记录日志，如果打开日志，要及时清理
log-queries
log-facility=/var/log/dnsmasq.log
#启用异步日志记录，缓解阻塞，提高性能。默认队列长度为5，合理值为5-25，最大限制为100
log-async=20

#缓存地址数目,提高速
cache-size=10000
#自动加载目录配置
conf-dir=/etc/dnsmasq.d12345678910111213141516171819202122232425262728293031323334353637

在/etc/dnsmasq.d目录下配置自定义项 
vi  server.conf  #配置nameserver

# 指定dnsmasq默认查询的上游服务器
server=8.8.8.8
#可以将特定的域名指定解析它的nameserver。一般是其他的内部DNS name server
server=/baidu.com/61.135.165.235
#指定反向DNS 192.168.1/24网段到192.168.2.1 dns查询
#server=/192.168.1.in-addr.arpa/192.168.2.1
#cn上游dns
server=/cn/114.114.114.11412345678

vi address.conf  #配置自定义nameserver



#指定domain解析地址
address=/www.test.net/127.0.0.1
#*.test.net匹配
address=/test.net/127.0.0.1
address=/.abc.com/1.1.1.1
address=/ipv6.test.com/fe80::20d:60ff:fe36:f83123456



对参数的解释

resolve-file　　   定义dnsmasq从哪里获取上游DNS服务器的地址， 默认是从/etc/resolv.conf获取。

strict-order　　   表示严格按照resolv-file文件中的顺序从上到下进行DNS解析，直到第一个解析成功为止。

listen-address     定义dnsmasq监听的地址，默认是监控本机的所有网卡上。局域网内主机若要使用dnsmasq服务时，指定本机的IP地址。

address　　　　  启用泛域名解析，即自定义解析a记录，如下配置为demon.com这个域名：

address=/demon.com/127.0.0.1  #访问demon.com时的所有域名都会被解析成127.0.0.1

bogus-nxdomain  为防止DNS污染，使用参数定义的DNS解析的服务器。注意：如果是阿里云服务器上配置dnsmasq要启用此项。

server　　　　　　指定dnsmasq程序使用哪个DNS服务器进行解析。       对于不同的网站可以使用不同的域名对应解析如下配置

server=/google.com/8.8.8.8    #表示对于google的服务，使用谷歌的DNS解析。

以上配置完毕后，需要重启dnsmasq服务，重启完毕后局域网中的其他机器，就可以通过该DNS服务器解析公网的域名。


3、启动服务

service dnsmasq start 
可以通过dig命令查询解析是否正确，如：

C:\Users\Administrator>dig @192.168.145.134  www.zhutw.com

; <<>> DiG 9.7.2rc1 <<>> @192.168.145.134 www.zhutw.com
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12080
;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;www.zhutw.com.                 IN      A

;; ANSWER SECTION:
www.zhutw.com.          0       IN      A       1.1.1.1

;; Query time: 4 msec
;; SERVER: 192.168.145.134#53(192.168.145.134)
;; WHEN: Mon May 22 22:50:52 2017
;; MSG SIZE  rcvd: 47

---------------------

本文来自 slimina 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/zhu_tianwei/article/details/72632078?utm_source=copy 