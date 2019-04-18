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

/*
  4  * Licensed to the Apache Software Foundation (ASF) under one
  5  * or more contributor license agreements. See the NOTICE file
  6  * distributed with this work for additional information
  7  * regarding copyright ownership. The ASF licenses this file
  8  * to you under the Apache License, Version 2.0 (the
  9  * "License"); you may not use this file except in compliance
 10  * with the License. You may obtain a copy of the License at
 11  *
 12  *   http://www.apache.org/licenses/LICENSE-2.0
 13  *
 14  * Unless required by applicable law or agreed to in writing,
 15  * software distributed under the License is distributed on an
 16  * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 17  * KIND, either express or implied. See the License for the
 18  * specific language governing permissions and limitations
 19  * under the License.
 20  */

import (
	"context"
	"crypto/tls"
	"fmt"
	"tutorial"
	
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
	return err
}

func runClient(transportFactory thrift.TTransportFactory, protocolFactory thrift.TProtocolFactory, addr string, secure bool) error {
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
	return handleClient(tutorial.NewCalculatorClient(thrift.NewTStandardClient(iprot, oprot)))
}
