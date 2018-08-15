# 定义函数

from abstest import your_abs

a = your_abs
print(a(-19))

# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass

# 参数检查
b = your_abs
b(-2)

# 返回多个值 其实返回的就是个tuple
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x,',', y)

r = move(100, 100, 60, math.pi / 6)
print(r)

# practice
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。
# 提示：计算平方根可以调用math.sqrt()函数：

import math
def quadratic(a, b, c):
    if not isinstance(a,(int,float)):
        raise TypeError("只能为整数或小数")
    if not isinstance(b,(int,float)):
        raise TypeError("只能为整数或小数")
    if not isinstance(c,(int,float)):
        raise TypeError("只能为整数或小数")
    result1 = (math.sqrt(b * b - 4 * a * c) - b) / (2 * a)
    result2 = (-math.sqrt(b * b - 4 * a * c) - b) / (2 * a)
    return result1, result2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')