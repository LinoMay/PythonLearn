# 循环

names = ['Michael', 'Lino', 'Lucy']
for name in names:
    print(name)

# range()函数，可以生成一个整数序列,从0开始
# 再通过list()函数可以转换为list
a = range(5)
b =list(a)
print(b)
sum = 0
for s in b:
    sum += s
print(sum)

# while

um = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break
for s in range(5):
    if s == 2:
        break
    print(s)

# continue
for s in range(5):
    if s == 2:
        continue
    print(s)