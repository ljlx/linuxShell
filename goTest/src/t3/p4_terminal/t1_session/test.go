/*
--------------------------------------------------
 File Name: test.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-28-下午6:22
---------------------说明--------------------------

---------------------------------------------------
*/

package t1_session

import (
	// TODO 使用国内镜像来下载go包
	// https://www.golangtc.com/t/56f3c175b09ecc66b9000181
	//  "golang.org/x/crypto/ssh/terminal"
	// go get -t github.com/golang/crypto/ssh/terminal
	// The -t flag instructs get to also download the packages required to build
	// the tests for the specified packages.
	// -t 参数意思应该是 下载依赖包
	// "github.com/golang/crypto/ssh/terminal"
	// "io"
	
	"golang.org/x/crypto/ssh"
	"fmt"
	
	"os"
	"net"
	"bytes"
	"log"
	"time"
	"io"
	"golang.org/x/crypto/ssh/terminal"
	"reflect"
	
	"strings"
	"path/filepath"
	// "net/http"
	"io/ioutil"
	"crypto/md5"
	"os/user"
)

type Cli struct {
	// ip地址
	Ip string
	// 端口,默认22
	port int
	// 用户
	username string
	// 密码
	passwd string
	// ssh客户终端
	sshclient *ssh.Client
	// 最近一次run的结果
	lastResult string
}

func (c *Cli) connect() (err error) {
	
	var (
		client *ssh.Client
		// session *ssh.Session
	)
	
	// authMethosSlice := make([]ssh.AuthMethod, 1)
	// authMethosSlice = append(authMethosSlice, ssh.Password(c.passwd))
	authMethosSlice := []ssh.AuthMethod{ssh.Password(c.passwd)}
	//
	// myhostKeyCallback := func(hostname string, remote net.Addr, pubkey ssh.PublicKey) error {
	// 	fmt.Printf("callback...")
	// 	return nil }
	//
	clientConfig := &ssh.ClientConfig{
		User: c.username,
		Auth: authMethosSlice,
		
		Timeout:         1 * time.Minute,
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
	}
	// 配置和连接信息准备好.开始连接...
	// // The network must be "tcp", "tcp4", "tcp6", "unix" or "unixpacket".
	/*
	case "tcp", "tcp4", "tcp6":
		case "udp", "udp4", "udp6":
		case "ip", "ip4", "ip6":
			if needsProto {
				return "", 0, UnknownNetworkError(network)
			}
		case "unix", "unixgram", "unixpacket":
	 */
	addr := fmt.Sprintf("%s:%d", c.Ip, c.port)
	if client, err = ssh.Dial("tcp", addr, clientConfig); err != nil {
		fmt.Fprintf(os.Stderr, "error to connect ,%v", err)
		return err
	}
	c.sshclient = client
	// if session, err = c.sshclient.NewSession(); err != nil {
	// 	return err
	// }
	// session.Run("ifconfig")
	return nil
}

func (c Cli) Execu(shell string) (msg string, err error) {
	// if c.sshclient==nil{
	// 	if err:= {
	//
	// 	}
	// }
	if err = c.connect(); err != nil {
		
		fmt.Fprintf(os.Stderr, "error[%v]", err)
		return "链接失败", nil
	}
	
	session, err := c.sshclient.NewSession()
	if err != nil {
		return "", err
	}
	defer session.Close()
	
	buf, err := session.CombinedOutput(shell)
	c.lastResult = string(buf)
	return c.lastResult, err
	
}

/*
	创建command-Cli对象
 */
func New(ip string, port int, username string, passwd string) *Cli {
	cli := new(Cli)
	// cli:=&Cli{Ip:ip,port:port,username:username}
	cli.Ip = ip
	cli.username = username
	cli.passwd = passwd
	cli.port = port
	return cli
}

func SSHConnect(user, password, host string, port int) (*ssh.Session, error) {
	var (
		auth         []ssh.AuthMethod
		addr         string
		clientConfig *ssh.ClientConfig
		client       *ssh.Client
		session      *ssh.Session
		err          error
	)
	// get auth method
	auth = make([]ssh.AuthMethod, 0)
	auth = append(auth, ssh.Password(password))
	hostKeyCallbk := func(hostname string, remote net.Addr, key ssh.PublicKey) error { return nil }
	
	clientConfig = &ssh.ClientConfig{
		User: user,
		Auth: auth,
		// Timeout:             30 * time.Second,
		HostKeyCallback: hostKeyCallbk,
	}
	// connet to ssh
	addr = fmt.Sprintf("%s:%d", host, port)
	if client, err = ssh.Dial("tcp", addr, clientConfig); err != nil {
		return nil, err
	}
	// create session
	if session, err = client.NewSession(); err != nil {
		return nil, err
	}
	return session, nil
}

func runSsh() {
	var stdOut, stdErr bytes.Buffer
	session, err := SSHConnect("hanxu", "jjj", "127.0.0.1", 22)
	if err != nil {
		log.Fatal(err)
	}
	defer session.Close()
	session.Stdout = &stdOut
	session.Stderr = &stdErr
	
	// session.Run("if [ -d liujx/project ]; then echo 0; else echo 1; fi")
	session.Run("ifconfig")
	command_resp := stdOut.String()
	fmt.Printf("%v", command_resp)
	// command_resp2 := strings.Replace(command_resp, "\n", "", -1)
	// ret, err := strconv.Atoi(command_resp2)
	// if err != nil {
	// panic(err)
	// fmt.Fprintf(os.Stderr, "errorInfo:%v", err)
	// }
	// fmt.Printf("%d, %s\n", ret, stdErr.String())
}

func (cli *Cli) RunTerminal(shell string, stdin io.Reader, stdout, stderr io.Writer) (err error) {
	var (
		session                         *ssh.Session
		oldstate                        *terminal.State
		terminal_width, terminal_height int
	)
	if cli != nil {
		if err = cli.connect(); err != nil {
			return err
		}
		if session, err = cli.sshclient.NewSession(); err != nil {
			return err
		}
		defer session.Close()
		//
		osfd := os.Stdin.Fd()
		fd := int(osfd)
		fdIsTerminal := terminal.IsTerminal(fd)
		if oldstate, err = terminal.MakeRaw(fd); err != nil {
			fmt.Fprintf(os.Stderr, "[fd:%v],error:%v \n", oldstate, err)
			return err
		}
		fmt.Printf("IsTerminal:{%v}, oldState:{%v} \n", fdIsTerminal, oldstate)
		// TODO 这些操作是什么意思? 需要系统了解terminal这个玩意儿.
		defer terminal.Restore(fd, oldstate)
		//
		session.Stdin = stdin
		session.Stdout = stdout
		session.Stderr = stderr
		//
		if terminal_width, terminal_height, err = terminal.GetSize(fd); err == nil {
			fmt.Printf("terminal_width:{%v}, terminal_height:{%v} \r\n", terminal_width, terminal_height)
		}
		// set up terminal modes
		terminal_modes := ssh.TerminalModes{
			ssh.ECHO:          1,     // enable echo
			ssh.TTY_OP_ISPEED: 14400, // input speed = 14.4kbaud
			ssh.TTY_OP_OSPEED: 14400, // input speed = 14.4kbaud
		}
		termStr := "xterm-256color"
		fmt.Printf("jaowiejfw \r\n")
		fmt.Printf("jaowiejfw \n")
		fmt.Printf("jaowiejfw \r\n")
		fmt.Printf("is ready to requestPty. term:[%v], height:[%v],width:[%v],modes:[%v] \n", termStr, terminal_height, terminal_width, terminal_modes)
		
		if err = session.RequestPty(termStr, terminal_height, terminal_width, terminal_modes); err != nil {
			log.Fatalf("session.requestPty has error.%v", err)
			return err
		}
		// fmt.Printf("cmd: ls / . output:[%v] \r\n", cli.exec(session, "ls /"))
		// fmt.Printf("cmd: pwd . output:[%v] \r\n", cli.exec(session, "pwd"))
		
		fmt.Printf("is ready to run shell: [%v] \r\n", shell)
		session.Run(shell)
	}
	
	return err
}

func (cli *Cli) exec(session *ssh.Session, command string) string {
	var (
		msg []byte
		err error
	)
	// TODO 几种执行命令方式的不同之处?
	// msg, err = session.CombinedOutput(command)
	msg, err = session.Output(command)
	//
	if err != nil {
		fmt.Printf("err message:%v \r\n", err)
		return ""
	} else {
		return string(msg)
	}
}

type StdProxy struct {
	nametag string
	reader  io.Reader
	writer  io.Writer
	logfile *os.File
}

func (proxy *StdProxy) InfoStr() string {
	var target interface{}
	if proxy.reader != nil {
		target = proxy.reader
	} else if proxy.writer != nil {
		target = proxy.writer
	}
	return fmt.Sprintf("name:[%v],target:[%v],targetType:[%v]", proxy.nametag, target, reflect.TypeOf(target))
}

func (proxy *StdProxy) Read(p []byte) (n int, err error) {
	pReader := proxy.reader
	// fmt.Printf("read before %v \n",p)
	n, err = pReader.Read(p)
	// return 0, nil
	if n > 0 {
		readtext := p[:n]
		proxy.logfile.Write(readtext)
		// fmt.Printf("read after %v \n", readtext)
	}
	
	return n, err
}

func (proxy *StdProxy) Write(p []byte) (n int, err error) {
	pWriter := proxy.writer
	n, err = pWriter.Write(p)
	if err == nil && n > 0 {
		currOutput := p[:n]
		// outputStr := string(currOutput)
		proxy.logfile.Write(currOutput)
		// proxy.logfile.WriteString(outputStr)
	} else {
		fmt.Printf("没有读取到数据,或者是有错误.number:[%v] err:[%v]", n, err)
	}
	return n, err
}

func proxyReader(nameTag string, targetReader io.Reader) io.Reader {
	
	// TODO 如何从哪个包里取一个常量来表示当前文件系统,使用那一种回车换行符
	//
	fmt.Printf("开始创建日志文件.")
	logfile, err := getLogPath("input.log")
	if err == nil {
		fmt.Printf("创建日志文件成功")
		proxy := &StdProxy{nametag: nameTag, reader: targetReader}
		fmt.Printf("proxy:[%v],targetInfo:[%v] \n", proxy, proxy.InfoStr())
		logfile.WriteString("begin: \n")
		proxy.logfile = logfile
		return proxy
	} else {
		fmt.Printf("创建日志文件失败:%v", err)
	}
	return nil
	
}

func getLogPath(logname string) (file *os.File, err error) {
	// 	/tmp/ioproxy
	filepathstr := os.TempDir()
	filepathstr = filepath.Join(filepathstr, "ioproxy")
	os.MkdirAll(filepathstr, 0700)
	filepathstr = filepath.Join(filepathstr, logname)
	return os.OpenFile(filepathstr, os.O_CREATE|os.O_APPEND|os.O_RDWR, 0700)
}

func proxyWriter(nameTag string, targetWriter io.Writer) *StdProxy {
	fmt.Printf("开始创建日志文件.")
	
	logfile, err := getLogPath("output.log")
	if err == nil {
		fmt.Printf("创建日志文件成功")
		proxy := &StdProxy{writer: targetWriter, nametag: nameTag}
		fmt.Printf("proxy:[%v],targetInfo:[%v] \n", proxy, proxy.InfoStr())
		logfile.WriteString("begin: \n")
		proxy.logfile = logfile
		return proxy
	} else {
		fmt.Printf("创建日志文件失败:%v", err)
	}
	return nil
}

/*
 使用终端发送命令,和交互式shell使用, 代理ssh并保存日志
 */
func testCase1() {
	shells := os.Args[1:]
	cli := New("192.168.0.51", 22, "hanxu", "jjj")
	// respText, _ := cli.Execu("ifconfig")
	// fmt.Printf("执行命令:%v", respText)
	// sss:=&os.Stdout
	// shell := "ssh lijie@192.168.0.31"
	shell := strings.Join(shells, " ")
	fmt.Printf("执行命令:%v \n", shells)
	pReaderIn := proxyReader("osInput", os.Stdin)
	pWriterOut := proxyWriter("osOutput", os.Stdout)
	pWriterErr := proxyWriter("osError", os.Stderr)
	defer pWriterOut.logfile.Close()
	defer pWriterErr.logfile.Close()
	//
	
	//
	error := cli.RunTerminal(shell, pReaderIn, pWriterOut, pWriterErr)
	// fmt.Fprintf(os.Stderr,"",error)
	if error != nil {
		log.Fatalf("发生了错误:%v \n", error)
	}
	
}

// ----------start----------结构体----------start----------

type PublicKeyResult struct {
	success      bool
	comment      string
	sshPublicKey *ssh.PublicKey
	sshOptions   *[]string
}

type AuthContext struct {
	authPublicKeysMap map[string]*PublicKeyResult
	privateKeysSigner ssh.Signer
}

func NewAuthContext() *AuthContext {
	authcontext := new(AuthContext)
	authcontext.authPublicKeysMap = make(map[string]*PublicKeyResult)
	return authcontext
}

// ----------end------------结构体----------end------------

var (
	loggerInfo  = log.New(os.Stdout, "info", log.LstdFlags)
	loggerError = log.New(os.Stderr, "error", log.LstdFlags)
)

/*
ssh登陆方式-密码认证
 */
func obtainAuthPasswdCallback() (func(conn ssh.ConnMetadata, password []byte) (*ssh.Permissions, error)) {
	
	return func(conn ssh.ConnMetadata, password []byte) (*ssh.Permissions, error) {
		// Should use constant-time compare (or better, salt+hash) in
		// a production setting.
		// 这里可以实现用户登陆机制.这里传的密码是明文的吧应该.
		// TODO 如何在代码上用标准库的api直接获取当前系统应该使用是什么换行符.而不用自己判断系统类型来拼接换行符.
		fmt.Printf("用户passwd登陆:sessionId:[%v],reqIp:[%v],username:[%v],passwd:[%v],clientVersion:[%v] \n", conn.SessionID(), conn.RemoteAddr(), conn.User(), string(password), conn.ClientVersion())
		// user: hx, passwd: hhh
		if strings.EqualFold(conn.User(), "hx") && strings.EqualFold(string(password), "hx") {
			return nil, nil
		} else {
			return nil, fmt.Errorf("passwd rejected for user [%v] \n", conn.User())
		}
	}
}

/*
ssh登陆方式-公私钥对配置方式.
 */
func obtainAuthPublicKeyCallback(ctx *AuthContext) (func(conn ssh.ConnMetadata, pubkey ssh.PublicKey) (*ssh.Permissions, error)) {
	
	return func(conn ssh.ConnMetadata, pubkey ssh.PublicKey) (*ssh.Permissions, error) {
		sshpublicKey, sshComment, _, _, err := ssh.ParseAuthorizedKey(pubkey.Marshal())
		if err != nil {
			loggerError.Printf("pubkey登陆错误信息:%v,v", sshpublicKey, err)
		}
		pubkeyText := string(sshComment)
		// fmt.Printf("用户登陆-公钥方式:类型[%v],公钥内容:[%v] \n", pubkey.Type(), pubkeyText)
		fmt.Printf("用户publicKey登陆:sessionId:[%v],reqIp:[%v],username:[%v],pubKeyType:[%v],pubkey:[%v],clientVersion:[%v] \n", string(conn.SessionID()), conn.RemoteAddr(), conn.User(), pubkey.Type(), pubkeyText, string(conn.ClientVersion()))
		//
		switch pubkey.Type() {
		case "test":
			return nil, nil
		case "ssh-rsa":
			pubkeyResu := ctx.authPublicKeysMap[fmt.Sprintf("%x", md5.Sum(pubkey.Marshal()))]
			
			if pubkeyResu != nil && pubkeyResu.success {
				sshperm := new(ssh.Permissions)
				sshperm.Extensions = map[string]string{
					"pubkey-fp": ssh.FingerprintSHA256(pubkey),
				}
				return sshperm, nil
			}
			return nil, fmt.Errorf("unknown public key for %v", conn.User())
		}
		
		return nil, nil
	}
	
}

func obtainAuthContext() (authCtx *AuthContext, err error) {
	ctx := NewAuthContext()
	// 受信任的客户公钥授权keys,允许这些用户登陆服务器
	// currUser:=TODO
	curruser, err := user.Current()
	fmt.Printf("获取当前用户:%v \n", curruser)
	dir_ssh := filepath.Join(curruser.HomeDir, ".ssh")
	authkeysFilePath := filepath.Join(dir_ssh, "authorized_keys")
	authkeysBytes, err := ioutil.ReadFile(authkeysFilePath)
	if err != nil {
		loggerError.Fatalf("failed to read file [%v],err:%v \n", authkeysFilePath, err)
	}
	// (out PublicKey, comment string, options []string, rest []byte, err error)
	fmt.Printf("成功获取到授权文件[%v],大小[%v] md5[%x] ,开始进行解析...\n", authkeysFilePath, len(authkeysBytes), md5.Sum(authkeysBytes))
	for len(authkeysBytes) > 0 {
		sshpublicKey, sshComment, sshOptions, restNext, err := ssh.ParseAuthorizedKey(authkeysBytes)
		if err != nil {
			if strings.ContainsAny(string(authkeysBytes), "no & key & found") {
				break
			}
			loggerError.Fatalf("ParseAuthorizedKey has been err,%v", err)
		}
		// 通过阅读源码的方式看到,rest实际上是authkeysBytes剩下的数据,
		authkeysBytes = restNext
		pubKeyResu := new(PublicKeyResult)
		pubKeyResu.success = true
		pubKeyResu.comment = sshComment
		pubKeyResu.sshPublicKey = &sshpublicKey
		pubKeyResu.sshOptions = &sshOptions
		
		pubkeyMapkey := fmt.Sprintf("%x", md5.Sum(sshpublicKey.Marshal()))
		ctx.authPublicKeysMap[string(pubkeyMapkey)] = pubKeyResu
		fmt.Printf("解析成功sshpubKey:[%v],md5-Marshal:[%v] \n", sshComment, pubkeyMapkey)
	}
	loggerInfo.Printf("解析受信任的客户公钥授权文件完成[%v]\n", authkeysFilePath)
	// 解析服务器私钥,每一个ssh服务器都需要一个公私钥对.
	// ssh服务器和客户机在建立连接的时候 会交换各自的公钥.通信时,会使用对方的公钥进行加密,用自己的私钥来进行解密交换信息.
	//
	// TODO 无法使用系统自带的etc目录下的, 需要研究下 如何通过这个库来自动生成ssh公私钥对.
	// sshServerRsaPrivateKeyFilePath := filepath.Join(string(filepath.Separator),"etc", "ssh", "ssh_host_rsa_key")
	sshServerRsaPrivateKeyFilePath := filepath.Join(dir_ssh, "proxyServer", "proxy_rsa_key.pri")
	if privateKeys, err := ioutil.ReadFile(sshServerRsaPrivateKeyFilePath); err != nil {
		loggerError.Fatalf("无法访问服务器私钥文件:%v \n,err:%v", sshServerRsaPrivateKeyFilePath, err)
	} else {
		// ssh.ParsePrivateKey()
		// ssh.ParsePrivateKeyWithPassphrase()
		ctx.privateKeysSigner, err = ssh.ParsePrivateKey(privateKeys)
		if err != nil {
			loggerError.Fatalf("解析服务器私钥文件失败:%v")
		}
	}
	
	return ctx, err
}

func AuthLogger(conn ssh.ConnMetadata, method string, err error) {
	
	fmt.Printf("AuthLogger...")
}

func BannerHello(conn ssh.ConnMetadata) string {
	
	fmt.Printf("BannerHello...")
	return "hello."
}

func obtainServerConfig(authctx *AuthContext) *ssh.ServerConfig {
	serverConfig := &ssh.ServerConfig{
		// 注册各种回调函数
		// Remove to disable password auth,如果没配置对应的callback,相当于禁用对应的认证方式.
		PasswordCallback:  obtainAuthPasswdCallback(),
		PublicKeyCallback: obtainAuthPublicKeyCallback(authctx),
		AuthLogCallback:   AuthLogger,
		BannerCallback:    BannerHello,
		//
		MaxAuthTries: 2,
	}
	return serverConfig
}

/*
测试
 */
func testCase2_ssh_server() (err error) {
	var (
		authctx *AuthContext
		server  net.Listener
	)
	
	// ----------start----------设置sshServerConfig----------start----------
	authctx, err = obtainAuthContext()
	if err != nil {
		loggerError.Fatalf("解析authcontext失败..%v", err)
	}
	serverConfig := obtainServerConfig(authctx)
	serverConfig.AddHostKey(authctx.privateKeysSigner)
	// Once a ServerConfig has been configured, connections can be accepted.
	// ----------end------------设置sshServerConfig----------end------------
	
	serverListenProtocol := "tcp"
	serverListenIp := "0.0.0.0"
	serverListenPort := "1234"
	serverListenHost := serverListenIp + ":" + serverListenPort
	//
	// server, err = cli.sshclient.Listen(serverListenProtocol, serverListenHost)
	
	server, err = net.ListenTCP("tcp4", &net.TCPAddr{IP: net.IPv4(0, 0, 0, 0), Port: 1234})
	
	if err != nil {
		loggerError.Fatalf("开启sshServer监听失败:[%v],err:%v", serverListenHost, err)
	} else {
		loggerInfo.Printf("开启sshServer成功... 监听: %v://%v \n", serverListenProtocol, serverListenHost)
	}
	// // Serve HTTP with your SSH server acting as a reverse proxy.
	// http.Serve(l, http.HandlerFunc(func(resp http.ResponseWriter, req *http.Request) {
	//    fmt.Fprintf(resp, "Hello world!\n")
	// }))
	// http.Serve(server, http.HandlerFunc(func(resp http.ResponseWriter, req *http.Request) {
	// 	fmt.Fprintf(resp, "hello.world \n")
	// }))
	//
	// ----------start----------loop-service----------start----------
	for {
		netconn, err := server.Accept()
		if err != nil {
			loggerError.Printf("failed to accept incoming connection: ", err)
			continue
		} else {
			loggerInfo.Printf("accept conn with client...")
		}
		defer func() {
			exception := recover()
			loggerError.Printf("发生了错误:%v", exception)
		}()
		err = testCase2_ssh_server_handrequest(&netconn, serverConfig)
		
	}
	// ----------end------------loop-service----------end------------
	
	return err
}

func testCase2_ssh_server_handrequest(netconn *net.Conn, serverConfig *ssh.ServerConfig) (err error) {
	// Before use, a handshake must be performed on the incoming
	// net.Conn.
	// 进行握手,与客户端建立ssh连接
	serverConn, channelNew, chanReq, err := ssh.NewServerConn(*netconn, serverConfig)
	
	if err != nil {
		loggerError.Printf("failed to handshake: ", err)
		return err
	}
	
	loggerInfo.Printf("客户端请求:ip[%v],clientVer:[%v],sessionId:[%v],user:[%v]", serverConn.RemoteAddr(), serverConn.ClientVersion(), serverConn.SessionID(), serverConn.User())
	//
	loggerInfo.Printf("logged in with permissions %v", serverConn.Permissions.Extensions)
	//
	// The incoming Request channel must be serviced.为什么是请求的通道作为一个异步服务对象?
	go ssh.DiscardRequests(chanReq)
	
	// Server the incoming Channel channel.
	//
	for channelItem := range channelNew {
		// Channels have a type, depending on the application level
		// protocol intended. In the case of a shell, the type is
		// "session" and ServerShell may be used to present a simple
		// terminal interface.
		if false == strings.EqualFold(channelItem.ChannelType(), "session") {
			// 通道类型不是session的拒绝掉,在这个用例中是一个shell, 类型是"session"
			channelItem.Reject(ssh.UnknownChannelType, "hx:UnknownChannelType:不是有效的shell通道类型,it is not a valid channelType,is support: (session)")
			continue
		}
		var (
			channel  ssh.Channel
			requests <-chan *ssh.Request
		)
		channel, requests, err = channelItem.Accept()
		if err != nil {
			loggerError.Printf("Could not accept channel:%v", err)
		}
		// Sessions have out-of-band requests such as "shell",
		// "pty-req" and "env".  Here we handle only the
		// "shell" request.
		go func(in <-chan *ssh.Request) {
			// item := <-in
			for reqShell := range in {
				// var payload []byte
				// wantreply := reqShell.WantReply
				// if wantreply {
				loggerInfo.Printf("reqshell:%v", reqShell)
				// isok := strings.EqualFold(reqShell.Type, "shell")
				// reqShell.Reply(isok, payload)
				reqShell.Reply(true, nil)
				// } else {
				// 	loggerInfo.Printf("客户端不需要reply,WantReply:false")
				// }
			}
		}(requests)
		// 哈哈 这应该就是平常看到的别人实现的交互式终端了.越来越接近底层终端了.
		// bash环境的PS1变量,应该就是在这个提示符(prompt) > 这里下手的.
		//
		term := terminal.NewTerminal(channel, ">")
		term.Write([]byte("testterminal,hello,terminal,你好. \n"))
		go func(cliTerminal *terminal.Terminal) {
			defer channel.Close()
			loggerInfo.Printf("进入这里了..")
			for {
				line, err := cliTerminal.ReadLine()
				if err != nil {
					loggerInfo.Printf("又退出了..")
					break
				}
				loggerInfo.Printf("哈哈哈,服务器输出了用户在终端输入的内容:%v \n", line)
				// 还可以设置自动完成的回调信息
				// term.AutoCompleteCallback
				var bufresp []byte
				bufresp = []byte(fmt.Sprintf("iam a resp:%v \n", line))
				cliTerminal.Write(bufresp)
			}
		}(term)
	}
	return nil
}

func Main() {
	// runSsh()
	// testCase1()
	testCase2_ssh_server()
}
