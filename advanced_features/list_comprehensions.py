__author__ = 'milton'
#coding=utf-8
import os

L = [x * x for x in range(1, 11) if x % 2 == 1]
print(L)

S = [m + n for m in 'ABC' for n in 'XYZ']
print(S)

D = [d for d in os.listdir('.')]
print(D)

d = {'a': 1, 'b': 2, 'c': 3}
A = [k + '=' + str(v) for k, v in d.iteritems()]
print(A)

U = ['Hello', 'World', 'MicroSoft', 'IBM', 1]
LO = [s.lower() for s in U if isinstance(s, str)]
print(LO)