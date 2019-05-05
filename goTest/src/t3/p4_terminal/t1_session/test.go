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

func Main() {
	// runSsh()
	shells := os.Args[1:]
	cli := New("127.0.0.1", 22, "hanxu", "jjj")
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
