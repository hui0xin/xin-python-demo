#!/usr/bin/python3

"""
标准数据类型
Python3 中有六个标准的数据类型：
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）
"""

print("------->Number（数字）")
"""
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
像大多数语言一样，数值类型的赋值和计算都是很直观的。
内置的 type() 函数可以用来查询变量所指的对象类型。
isinstance 和 type 的区别在于：
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
"""

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

# 此外还可以用 isinstance 来判断
print(isinstance(a, int))

"""
Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
"""

print(issubclass(bool, int))
print(True==1)
print(False==0)
print(True+1)
print(False+1)
print(1 is True)
print(0 is False)

"""
当你指定一个值时，Number 对象就会被创建：
var1 = 1
您可以通过使用del语句删除单个或多个对象。例如：
del var
del var_a, var_b
"""
print("1------->基本运算")
print(5 + 4) # 加法
print(4.3 - 2) # 减法
print(3 * 7) # 乘法
print(2 / 4) # 除法，得到一个浮点数 0.5
print(2 // 4) # 除法，得到一个整数 0
print(17 % 3) # 取余 2
print(2 ** 5) # 乘方 32

"""
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4、在混合计算时，Python会把整型转换成为浮点数。
"""

