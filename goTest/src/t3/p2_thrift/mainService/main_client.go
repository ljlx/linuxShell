/*
--------------------------------------------------
 File Name: main_client.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-4-18-下午9:36
---------------------说明--------------------------

---------------------------------------------------
*/

package mainService

import (
	"context"
	"crypto/tls"
	"fmt"
	
	"t3/p2_thrift/go_thrift/gen-go/tutorial"
	
	"github.com/apache/thrift/lib/go/thrift"
)

// tutorials  n. 教程；专题报告；学习指南（tutorial的复数） 网络释义:

var defaultCtx = context.Background()

func handleClient(client *tutorial.CalculatorClient) (err error) {
	
	client.Ping(defaultCtx)
	fmt.Println("ping()")
	sum, _ := client.Add(defaultCtx, 1, 1)
	fmt.Print("1+1=", sum, "\n")
	work := tutorial.NewWork()
	work.Op = tutorial.Operation_SUBTRACT
	work.Num1 = 15
	work.Num2 = 10
	diff, err := client.Calculate(defaultCtx, 1, work)
	if err != nil {
		switch v := err.(type) {
		case *tutorial.InvalidOperation:
			fmt.Println("Invalid operation:", v)
		default:
			fmt.Println("Error during operation:", err)
		}
		return err
	} else {
		fmt.Print("15-10=", diff, "\n")
	}
	log, err := client.GetStruct(defaultCtx, 1)
	if err != nil {
		fmt.Println("Unable to get struct:", err)
		return err
	} else {
		fmt.Println("Check log:", log.Value)
	}
	
	work.Op = tutorial.Operation_DIVIDE
	work.Num1 = 1
	work.Num2 = 0
	quotient, err := client.Calculate(defaultCtx, 1, work)
	if err != nil {
		switch v := err.(type) {
		case *tutorial.InvalidOperation:
			fmt.Println("Invalid operation:", v)
		default:
			fmt.Println("Error during operation:", err)
		}
		return err
	} else {
		fmt.Println("Whoa we can divide by 0 with new value:", quotient)
	}
	
	return err
}

func RunClient(transportFactory thrift.TTransportFactory, protocolFactory thrift.TProtocolFactory, addr string, secure bool) error {
	var transport thrift.TTransport
	var err error
	if secure {
		cfg := new(tls.Config)
		cfg.InsecureSkipVerify = true
		transport, err = thrift.NewTSSLSocket(addr, cfg)
	} else {
		transport, err = thrift.NewTSocket(addr)
	}
	if err != nil {
		fmt.Println("Error opening socket:", err)
		return err
	}
	transport, err = transportFactory.GetTransport(transport)
	if err != nil {
		return err
	}
	defer transport.Close()
	if err := transport.Open(); err != nil {
		return err
	}
	iprot := protocolFactory.GetProtocol(transport)
	oprot := protocolFactory.GetProtocol(transport)
	TClient := thrift.NewTStandardClient(iprot, oprot)
	MyCalculatorClient := tutorial.NewCalculatorClient(TClient)
	
	return handleClient(MyCalculatorClient)
}
