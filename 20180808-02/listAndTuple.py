# 使用list和tuple

# list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Lino', 'Sara']
classmates

# len()函数可以获得list元素的个数：
len(classmates)

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的：
classmates[0]

# 还可以用-1做索引，直接获取最后一个元素：
classmates[-1]
classmates[-2]

# list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Adam')
classmates

# 可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1, 'Jack')
classmates

# 要删除list末尾的元素，用pop()方法：
classmates.pop()
classmates

# 删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)

# 把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'May'
classmates

# list里面的元素的数据类型也可以不同，比如：
L = ['May', 123, True]
L

# list元素也可以是另一个list，比如：
L.insert(1,classmates)
L

# 一个list中一个元素也没有，就是一个空的list，它的长度为0：
S = []
S

# tuple
# tuple和list非常类似，但是tuple一旦初始化就不能修改

books = ('Love', 'Hate', 'Mercy')
books[0]
books[1]

# 当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t = (1, 2)
t

# 要定义一个空的tuple，可以写成()：
t = ()
t

# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
t[0]

# “可变的”tuple 本质上是tuple中放了一个list，list可变，但是list的引用没变
t = ('a', 'b', ['A', 'B'])
t[2][1] = 'C'
t

# practice 
# 请用索引取出下面list的指定元素：

# -*- coding: utf-8 -*-
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])