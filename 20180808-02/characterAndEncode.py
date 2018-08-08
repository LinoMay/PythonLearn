# 字符串和编码

# 字符编码
# ASCII编码是1个字节，而Unicode编码通常是2个字节
# UTF-8（“可变长编码”）编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，
# 常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节
# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

# Python的字符串支持多语言
print("包含中文的str")

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示
ord("A")
ord("中")
ord("文")
ord("の")

# chr()函数把编码转换为对应的字符
chr(66)
chr(10086)
chr(10088)

# 知道字符的整数编码，还可以用十六进制这么写str
'\u4e2d\u6587'

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes

# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
'ABC'.encode('ascii')
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示
'中文'.encode('utf-8')
# 错误示例
'中文'.encode('ascii')

# 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
b'ABC'.decode('ascii')

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
b'\xe4\xb8\xad\xe6\x96\x87\xab'.decode('utf-8', errors='ignore')

# 要计算str包含多少个字符，可以用len()函数：
len('ABC')
len('中文')

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
len(b'ABC')
len('中文'.encode('utf-8'))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。


# 格式化
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
'Hello,%s' % '字符串'
'hello,%f' % 1.14159
'hello, %d' % 6
'hello, %x' % 0xaa
'hello, %x' % 170
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1495926)

# %s永远起作用，它会把任何数据类型转换为字符串：
'Age: %s. Gender: %s' % (25, True)

# 用%%来表示一个%：
'growth rate: %d %%' % 7

# format() 它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
'Hello,{0},成绩提升了 {1:.1f}'.format('小明', 22.345)


# practice
s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print('小明成绩提升百分点为 %.1f %% ' % r)