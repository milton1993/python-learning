__author__ = 'milton'

s = set([1, 2, 3, 3, 2, 1])
print(s)

s.add(4)
s.remove(2)
s.add(1)
print(s)

s2 = set([3, 4, 5])
print(s & s2)
print(s | s2)