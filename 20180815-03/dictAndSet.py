# 使用dict和set

# dict类似json，key-value结构
d = {'Michael' : 99, 'Lino' : 98, 'Lucy' : 59}
d['Lino']

# 除了初始化时指定外，还可以通过key放入：
d['Adam'] = 66
d['Adam']

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
'Tomas' in d
'Lino' in d

# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('Lino')
d.get('Tomas')
d.get('Tomas', '没有值')
d.get('Lino', '没有值')

# 删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Adam')
d.get('Adam')

# dict内部存放的顺序和key放入的顺序是没有关系的。
# 和list比较，dict有以下几个特点：
#   查找和插入的速度极快，不会随着key的增加而变慢；
#   需要占用大量的内存，内存浪费多。
# 而list相反：
#   查找和插入的时间随着元素的增加而增加；
#   占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。

# dict的key必须是不可变对象
# 反例：
key = [1, 2, 3]
d[key] = 'a list'

# set 
# set和dict类似，也是一组key的集合，但不存储value。
# 由于key不能重复，所以，在set中，没有重复的key。
# 与java中的Set类似，相较于list，是个去重的集合。
# 创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
s = set([1, 1, 2, 2, 3, 3])

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(5)

# 通过remove(key)方法可以删除元素：
s.remove(5)

# 交集、并集 操作
s1 = set([1,2,4])
s2 = set([1,2,5])
s1 & s2
s1 | s2

# 同样不可以放入可变对象，因为无法判断两个可变对象是否相等，
# 也就无法保证set内部“不会有重复元素”
# 反例：
s = set([1, 2, 3])
s.add([2,3,2])