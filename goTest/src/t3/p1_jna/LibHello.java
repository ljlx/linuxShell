package com.vrv;

import java.util.*;
import java.lang.*;

import com.sun.jna.Library;
import com.sun.jna.Native;
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
 * @CreateDate 2019-04-03 上午11:40
 * @encode UTF-8
 * @needThreadSave false
 * @companySite <a href="https://gfyt.lan">访问公司主页</a>
 */
public interface LibHello extends Library
{
	
	LibHello INSTANCE = Native.loadLibrary("/data/project/code/personal/develop/linuxShell/goTest/src/t3/p1_jna/libhello.so", LibHello.class);
	
	/**
	 * 注意，Sum是函数名，一定要与Go中事先写好的函数名保持一致 Native.loadLibrary()的第一个参数是一个字符串，要加载的动态库的名称或全路径，后面不需要加.dll或者.so的后缀。第二个参数为interface的类名称。
	 *
	 * @param a
	 * @param b
	 * @return
	 */
	int Sum(int a, int b);
	
	GoString.ByReference HelloString(GoString.ByValue name);
	
	void HelloString2(GoString.ByValue name);
}
