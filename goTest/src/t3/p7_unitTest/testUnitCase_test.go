/*
--------------------------------------------------
 File Name: testUnitCase_test.go
 Author: hanxu
 AuthorSite: http://www.thesunboy.com/
 GitSource: https://github.com/thesunboy-com/linuxShell
 Created Time: 2019-5-13-下午4:15
---------------------说明--------------------------
 测试用例
---------------------------------------------------
*/

package testUnitCase

import (
	"fmt"
	"github.com/smartystreets/goconvey/convey"
	"math/rand"
	// "os"
	"testing"
)

func TestMain(m *testing.M) {
	fmt.Printf("setup code...")
	m.Run()
	fmt.Printf("teardown code...")
}

// 单元测试
// 测试全局函数,以Test+FunctionName命名
// 测试类成员函数,以TestClass_Function命名
func TestCombination(t *testing.T) {
	// 这里定义一个临时的结构体来存储测试case的参数及其期望的函数返回结果值.
	for _, unit := range []struct {
		// 声明匿名的结构体
		arg0        int
		arg1        int
		expectValue int
	}{
		// 为匿名的结构体,预定义一些值
		{1, 0, 1},
		{4, 1, 4},
		{4, 2, 6},
		{4, 3, 4},
		{4, 4, 1},
		{10, 1, 10},
		{10, 3, 120},
		{10, 7, 120},
	} {
		// for 循环体
		// 调用排列组合函数，与期望的结果比对，如果不一致输出错误
		if result := combination(unit.arg0, unit.arg1); result != unit.expectValue {
			// 计算结果与预期不符合.
			t.Errorf("combination(%v,%v)-> return [%v], but expect is [%v]  ", unit.arg0, unit.arg1, result, unit.expectValue)
		} else {
			formatlog := "combination(%v,%v)-> return [%v],test Ok! \n"
			// (unit.arg0, unit.arg1, result)
			
			// formatArgs := [...]interface{}{unit.arg0, unit.arg1, result}
			// TODO 参数数组在传进 ...interface{} 类型的行参时会被封装成一个参数. 将参数作为一个数组参数设置进去了.
			t.Logf(formatlog, unit.arg0, unit.arg1, result)
			fmt.Printf(formatlog, unit.arg0, unit.arg1, result)
		}
		
	}
}

/*
https://github.com/smartystreets/goconvey
*/
func TestAddAB(t *testing.T) {
	convey.Convey("give some integer with a starting value", t, func() {
		// x:=1
		// convey.conv
	})
}

// 性能测试
func BenchmarkCombination(b *testing.B) {
	// b.N会根据函数的运行时间取一个合适的值
	b.Logf("(基准测试)Benchmark: N->%v", b.N)
	lastN := b.N
	for i := 0; i < lastN; i++ {
		if lastN != b.N {
			b.Logf("change:(基准测试)Benchmark: N->%v", b.N)
			lastN = b.N
		}
		combination(i+1, rand.Intn(i+1))
	}
	
}

// 并发性能测试

func BenchmarkCombinationParallel(t *testing.B) {
	// 测试一个对象或者函数在多线程场景下是否安全.
	t.RunParallel(func(pb *testing.PB) {
		for pb.Next() {
			arg0 := rand.Intn(100) + 1
			arg1 := rand.Intn(arg0)
			combination(arg0, arg1)
		}
	})
	
}
