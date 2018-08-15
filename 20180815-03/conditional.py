# 条件判断

age = 20
if age >= 18:
    print("your age is", age)
    print("adult")

age = 3
if age >= 18:
    print("your age is", age)
    print("adult")
else:
    print("teenage")

age = 10
if age >= 18:
    print("your age is", age)
    print("adult")
elif age >=6:
    print("child")
else:
    print("teenage")

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = 10
if x:
    print("true")

# input()返回的数据类型是str，str不能直接和整数比较，
# 必须先把str转换成整数。
# Python提供了int()函数来完成这件事情
s = input("birth:")
birth = int(s)
if birth < 2000:
    print("00前")
else:
    print("00后")

# practice
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

height = 1.75
weight = 80.5
bmi = weight / (1.75 * 1.75)
print(bmi)
if bmi < 18.5:
    print("过轻")
elif bmi >= 18.5 and bmi < 25:
    print("正常")
elif bmi >= 25 and bmi < 28:
    print("过重")
elif bmi >= 28 and bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")