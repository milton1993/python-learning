__author__ = 'milton'
# -*- coding=utf-8 -*-

l = ['c', 'b', 'a']
l.sort()
print(l)

a = 'abc'
b = a.replace('b', 'B')
print(a)
print(b)

t = (1, 2, [3, 4])
# t[0] = 3 不可修改
t[2][0] = 2
print(t)