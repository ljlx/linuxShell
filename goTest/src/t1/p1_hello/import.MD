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