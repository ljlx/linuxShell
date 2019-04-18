/*
--------------------------------------------------
 File Name: Main.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-18-下午6:04
---------------------说明--------------------------
 go-thrift 测试http://thrift.apache.org/tutorial/go
---------------------------------------------------
*/
package main

import (
	"flag"
	"fmt"
	"os"
	
	"t3/p2_thrift/mainService"
	
	"github.com/apache/thrift/lib/go/thrift"
)

func Usage() {
	fmt.Fprint(os.Stderr, "Usage of ", os.Args[0], ":\n")
	flag.PrintDefaults()
	fmt.Fprint(os.Stderr, "\n")
}

func main() {
	
	flag.Usage = Usage
	server := flag.Bool("server", false, "Run server")
	protocol := flag.String("P", "binary", "Specify the protocol (binary, compact, json, simplejson)")
	framed := flag.Bool("framed", false, "Use framed transport")
	buffered := flag.Bool("buffered", false, "Use buffered transport")
	addr := flag.String("addr", "localhost:9090", "Address to listen to")
	secure := flag.Bool("secure", false, "Use tls secure transport")
	
	flag.Parse()
	
	var protocolFactory thrift.TProtocolFactory
	switch *protocol {
	case "compact":
		protocolFactory = thrift.NewTCompactProtocolFactory()
	case "simplejson":
		protocolFactory = thrift.NewTSimpleJSONProtocolFactory()
	case "json":
		protocolFactory = thrift.NewTJSONProtocolFactory()
	case "binary", "":
		protocolFactory = thrift.NewTBinaryProtocolFactoryDefault()
	default:
		fmt.Fprint(os.Stderr, "Invalid protocol specified", protocol, "\n")
		Usage()
		os.Exit(1)
	}
	
	var transportFactory thrift.TTransportFactory
	if *buffered {
		transportFactory = thrift.NewTBufferedTransportFactory(8192)
	} else {
		transportFactory = thrift.NewTTransportFactory()
	}
	
	if *framed {
		transportFactory = thrift.NewTFramedTransportFactory(transportFactory)
	}
	
	fmt.Printf("server:[%v] \n,addr:[%v] \n,secure:[%v] \n,protocolFactory:[%v] \n", server, addr, secure, protocolFactory)
	
	if *server {
		if err := mainService.RunServer(transportFactory, protocolFactory, *addr, *secure); err != nil {
			fmt.Println("error running server:", err)
		}
	} else {
		if err := mainService.RunClient(transportFactory, protocolFactory, *addr, *secure); err != nil {
			fmt.Println("error running client:", err)
		}
	}
}
