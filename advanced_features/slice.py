__author__ = 'milton'
#coding=utf-8

L = ['a', 'b', 'c', 'd', 'e']
print(L[0:3])
print(L[:2])
print(L[1:2])  #两个数都是index,但是是左闭右开区间
print(L[-3:-1])


numbers = range(100)
print(numbers[0:10:2])
print(numbers[::5]) #从头到尾每5个取1个
print(numbers[:])

T = (0, 1, 2, 3, 4, 5)
print(T[0:3])

S = 'ABCDEFG'
print(S[3:5])