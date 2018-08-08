# 数据类型和变量

# 字符串转义输出
print("I\'m \"OK\"!")

# \n 换行  \t 制表符
print("I\'m \"OK\"! \n And you ? \t hahaha")

# r''表示 ’‘内部字符串默认不转义
print(r'\\tta\n\\"')

# '''...'''表示多行内容,仅在命令交互框可用
print('''line1 
... line2 
... line3''')
# ''' '''表示多行内容,在.py文件可用
print('''line1 
line2 
line3''')


# practice
# 多行字符串'''...'''还可以在前面加上r使用，请自行测试：
print(r''' hello, \n
world ''')

# 布尔值
True
False
3 > 2
3 > 5
True and True
True and False
False and False

True or True
True or False
False or False

age = 19
if age > 18:
    print('adult')
else:
    print('teenager')

# 空值
None

# 变量 
# 无需确定变量类型，因此成为动态语言 ，Java为静态语言
# 动态语言更灵活
a = 123
print(a)
a = 'ABC'
print(a)

# 变量的本质是引用
# practice
a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 常量 通常在python中常量用大写表示
PI = 3.141592653

# / 除法 计算结果保留浮点数 
# // 取整数 不保留浮点数
# % 取余数

10 / 3
9 / 3
10 // 3
10 % 3