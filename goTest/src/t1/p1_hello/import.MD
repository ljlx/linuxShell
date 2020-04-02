## import规则
> 来源[imooc](https://www.imooc.com/video/16850)

* 如果一个main导入了其他包,包将被顺序导入
* 如果导入的(A)包还依赖了其他(B)包,会首先导入B包,然后顺序初始化B包中的常量,全局变量.  
  最后如果B包中有init函数,会执行init(),然后在按相同规则导入A包.
* 所有包导入完成后,才会对main中的常量和变量进行初始化,  
  然后执行main中的init函数(如果存在的话),最后执行main函数;
* 一个包只能被导入一次.

#### 两种语法:

1. 使用一对圆括号包括多个包名字符串.
```
import (
	"os"
	"strings"
	"fmt"
)
```

2. 使用类似java,python的语法,多行导入包.
```
import "os"
import "strings"
import "fmt"
```

#### import别名

1. 别名操作的含义是: 将导入的包命名为另一个容易记忆的别名.
2. 点( . )操作的含义是: 点( . )标识的包导入后,调用包中函数时可以省略前缀包名(不建议使用,容易造成不同包同名函数冲突,而且程序可读性降低.)
3. 下划线( _ )操作的含义是: 导入该包,但不导入整个包,而是执行包中的`init函数`,因此无法通过包名来调用包中其他函数.  
    使用下划线( _ )操作往往是为了注册包里的引擎,让外部可以方便的使用,类似安卓和java一些驱动包,在class加载的时候内部执行一些类的注册操作,
    将一些设计好的handler注册进全局常量中.  
    
**例子:**
```
package main

import (
	test "fmt"
	. "time"
	_ "os"
)
func main() {
	test.Print("test")
	println("start...")
	//time.Now()
	println("",Now().String())
	// 报错,方法无法使用,但是可以加载init函数.
	//println(os.Args[1])
}
```