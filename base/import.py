# three methods of import library
# module and package => package = modules, one python file can be a module

import this
import math as m    

print(m.gcd(4, 6))

from math import gcd
print(gcd(4, 6))

from math import gcd, sqrt  # 从 module 中引入 方法
from math import *  # all methods. tips: had better not

# function

def a_sub_function():  # 函数名全小写
    pass


# 推荐: 两个函数之间空两行
def add(m, n):
    return m + n  # python 中函数函数都有返回值, 无 return 即返回 None


print(add(n=2, m=3))  # 不要写成  n = 2 , 参数 顺便可变(带上参数名时)

def sub(m=5, n=1):  # 函数默认值, 有默认值的参数放在最后, 因为函数默认参数定义只能是从右往左依次定义的
    return m - n


def multiple(*args):  # args 可以随意命名, 是个元组
    tmp = 1

    for i in args:
        tmp *= i
    return tmp


m = multiple(1, 2, 3, 4)
print(m)


def mul02(**args):  # args 是字典
    tmp = 1

    for i in args:
        tmp *= args[i]
    return tmp


n = mul02(m=1, n=2, k=3)
print(n)

def mul03(*args, **k_args):  # args 必须写在 k_args 之前
    tmp = 1

    for i in args:
        tmp *= i

    for k in k_args:
        tmp *= k_args[k]
    return tmp


k = mul03(1, 2, m=3, n=4, k=5)
print(k)
