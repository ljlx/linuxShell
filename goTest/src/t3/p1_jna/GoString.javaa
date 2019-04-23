package com.vrv.dto;

import java.util.*;
import java.lang.*;

import com.sun.jna.Structure;
import org.apache.commons.lang3.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * <b>功能说明:</b><p>
 * 我们首先用JNA构建一个C的结构体类型，那么问题来了，JNA中char 可以直接用java的String来代替，那么ptrdiff_t这个玩意……有点无语，这是啥啊？经过一顿操作百度和谷歌，终于知道了，这个类型实际上是两个内存地址之间的距离的值，数据类型实际上就是C中的long int，在这里他表示的是字符串char 的长度，也就是字符串的长度呗~，知道这个就好办了，我们在Java中直接用long类型来代替它。 我们新建一个GoString类来对应C中的GoString结构体，也就是Go程序中的string，这块得说一下，有些人可能没有用过JNA，在JNA中若想定义一个结构体，需要创建一个类继承自com.sun.jna.Structure，熟悉C的人应该知道（不知道也没关系），向C中传值通常有两种，一种是传引用（就是传指针类型），一种是传真实值，在JNA里面做的话我们通常在这个结构体类中创建两个静态的内部类，这两个内部类继承自这个结构体类，并实现Structure.ByValue和Structure.ByReference接口，其中ByValue就是传真实值时候用的，ByReference就是传引用的时候用的，综上所述，我们的GoString类就应该长成这个样子：
 * </p></br> <b>设计思想、目的:</b><p>
 * 参考至:
 * https://studygolang.com/topics/6025/comment/17780
 * </p></br><b>设计缺陷: </b>
 * <p>
 * 一些说明写这里
 * </p>
 *
 * @author hanxu
 * @version 1.0
 * @CreateDate 2019-04-03 下午3:41
 * @encode UTF-8
 * @needThreadSave false
 * @companySite <a href="https://gfyt.lan">访问公司主页</a>
 */
public class GoString extends Structure
{
	//	在JNA中若想定义一个结构体，需要创建一个类继承自com.sun.jna.Structure
	public String str;
	public long length;
	
	public GoString() {}
	
	;
	
	public GoString(String str) {
		this.str = str;
		this.length = str.length();
	}
	
	@Override
	protected List<String> getFieldOrder() {
//		可以发现，我们重写了一个getFieldOrder方法，在里面新建一个list，然后把两个属性名作为字符串放到里面，然后当做返回值返回了。这个操作实际是为了告诉JNA，我这两个变量和C结构体中的变量是怎么个对应关系的，我们再来回顾一下刚才libhello.h中定义的GoString结构体（其实是省着你再往上翻看，费劲，直接粘出来方便你看）
		List<String> fields = new ArrayList<>();
		fields.add("str");
		fields.add("length");
		return fields;
	}
	
	public static class ByValue extends GoString implements Structure.ByValue
	{
		public ByValue() {
		
		}
		
		public ByValue(String str) {
			super(str);
		}
	}
	
	public static class ByReference extends GoString implements Structure.ByReference
	{
		public ByReference() {
		
		}
		
		public ByReference(String str) {
			super(str);
		}
	}
	
}
