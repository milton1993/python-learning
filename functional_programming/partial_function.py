__author__ = 'milton'
#coding=utf-8
import functools


#当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
def int2(x, base=2):
    return int(x, base=2)

print int2('10000')


int8 = functools.partial(int, base=8)

print(int8('50644'))


max2 = functools.partial(max, 10)

print max2(5,6,7)