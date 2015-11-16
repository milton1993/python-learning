__author__ = 'milton'
#coding=utf-8

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(1))

print(fact(999))

#解决递归栈溢出问题：尾递归，即return语句不包含表达式