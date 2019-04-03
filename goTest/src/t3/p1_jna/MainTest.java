package com.vrv;

import java.util.*;
import java.lang.*;

import com.vrv.dto.GoString;
import org.apache.commons.lang3.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * <b>功能说明:</b><p>
 * 一些说明写这里
 * </p></br> <b>设计思想、目的:</b><p>
 * 一些说明写这里
 * </p></br><b>设计缺陷: </b>
 * <p>
 * 一些说明写这里
 * </p>
 *
 * @author hanxu
 * @version 1.0
 * @CreateDate 2019-04-03 上午11:44
 * @encode UTF-8
 * @needThreadSave false
 * @companySite <a href="https://gfyt.lan">访问公司主页</a>
 */
public class MainTest
{
	private final Logger logger = LoggerFactory.getLogger(MainTest.class);
	
	public static void main(String[] args) {
		LibHello libHelloInstance = LibHello.INSTANCE;
		int sum = libHelloInstance.Sum(4, 5);
		System.out.println(sum);
		GoString.ByValue text = new GoString.ByValue("hanxuuu");
		GoString hanxulala = libHelloInstance.HelloString(text);
		//
		libHelloInstance.HelloString2(text);
		//		System.out.println(hanxulala);
		//		System.out.println(1);
	}
	
}
