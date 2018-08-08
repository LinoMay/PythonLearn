# PythonLearn

学一点，记录一点

## 第一个Python程序

### 输入和输出

* 输入函数 input()
* 输出函数 print()

## Python 基础

1. Python是`大小写敏感`；
2. 以`#`开头的语句是注释；
3. 以`:`结尾时，自下一行开始缩进的语句视为代码块，一般坚持使用`4个空格`的缩进；

### 数据类型和变量

* 整数
> 在程序中的表示方法和数学上的写法一模一样，例如：`1`，`100`，`-8080`，`0`，等等。十六进制用0x前缀和0-9，a-f表示，例如：`0xff00`，`0xa5b4c3d2`，等等。
* 浮点数
> 浮点数可以用数学写法，如`1.23`，`3.14`，`-9.01`，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，`1.23x109`就是`1.23e9`，或者`12.3e8`，`0.000012`可以写成`1.2e-5`，等等。  
整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。

* 字符串
> `“`， `‘` 都可， 转义使用 `\`

* 布尔值
> 取值范围：`True` `False`
> 运算符： `and` `or` `not`

* 空值
> None

* 变量
> 变量名必须是大小写英文、数字和_的组合，且不能用数字开头

* 常量
> 通常常量都以大写表示