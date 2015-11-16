__author__ = 'milton'
#coding=utf-8


#把函数作为返回值
def lazy_sum(*args):
    def real_sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return real_sum

f1 = lazy_sum(1, 2, 3, 4, 5)
f2 = lazy_sum(1, 2, 3, 4, 5)
print(f1 == f2)

print(f1())


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())  # 9
print(f2())  # 9
print(f3())  # 9

#返回函数不要引用任何循环变量，或者后续会发生变化的变量


#替换方案：再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count1():
    fs = []

    def f(j):
        def g():
            return j * j
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count1()
print(f1())  # 1
print(f2())  # 4
print(f3())  # 9


#使用lambda匿名函数简化
def count2():
    fs = []
    f = lambda z: lambda: z * z
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count2()
print(f1())
print(f2())
print(f3())