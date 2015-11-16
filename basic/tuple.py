__author__ = 'milton'
# -*- coding=utf-8 -*-

#tuple是不可变的list
t = (1, 2)
print(t)
print(len(t))

#只有一个元素时，返回的不是tuple，而是其中的元素
t = (1)
print(t)
#一个元素的tuple定义是必须加一个逗号，来消除歧义
t = (1,)
print(len(t))

#“可变”的tuple
t = (1, 2, ['X', 'Y'])
t[2][0] = 'A'
t[2][1] = 'B'
print(t)