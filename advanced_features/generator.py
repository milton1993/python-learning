__author__ = 'milton'
#coding=utf-8

g = (x * x for x in range(10))

for n in g:
    print(n)


#使用函数和yield定义生成器
def fib(max):
    m, a, b = 0, 0, 1
    while m < max:
        yield b
        a, b = b, a + b
        m += 1

for n in fib(6):
    print n
