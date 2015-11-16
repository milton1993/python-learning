__author__ = 'milton'
#coding=utf-8
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for value in d.itervalues():
    print(value)

for key, value in d.iteritems():
    print(key)
    print(value)

for ch in 'ABC':
    print(ch)


print(isinstance('ABC', Iterable))

print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):  #enumerate函数可以把list变成索引-元素对
    print i, value

for x, y in [(1, 2), (3, 4), (5, 6)]:
    print x, y