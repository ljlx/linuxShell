/*
--------------------------------------------------
 File Name: main_server.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-18-下午9:37
---------------------说明--------------------------
 server
---------------------------------------------------
*/

package mainService


import (
	"crypto/tls"
	"fmt"
	
	"t3/p2_thrift/go_thrift/gen-go/tutorial"
	
	"github.com/apache/thrift/lib/go/thrift"
)

func RunServer(transportFactory thrift.TTransportFactory, protocolFactory thrift.TProtocolFactory, addr string, secure bool) error {
	var transport thrift.TServerTransport
	var err error
	if secure {
		cfg := new(tls.Config)
		if cert, err := tls.LoadX509KeyPair("server.crt", "server.key"); err == nil {
			cfg.Certificates = append(cfg.Certificates, cert)
		} else {
			return err
		}
		transport, err = thrift.NewTSSLServerSocket(addr, cfg)
	} else {
		transport, err = thrift.NewTServerSocket(addr)
	}
	
	if err != nil {
		return err
	}
	fmt.Printf("%T\n", transport)
	handler := NewCalculatorHandler()
	processor := tutorial.NewCalculatorProcessor(handler)
	server := thrift.NewTSimpleServer4(processor, transport, transportFactory, protocolFactory)
	
	fmt.Println("Starting the simple server... on ", addr)
	return server.Serve()
}
