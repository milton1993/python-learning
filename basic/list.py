__author__ = 'milton'

a = ['abc', 'bbb', 1, True, ['a', 1.2]]

print a[2], a[-1][1]

print len(a)

a.append('ddd')

print(len(a))

a.insert(2, 'bb')

print(a[3])

print(a.pop())

print(len(a))

a = range(10)

print(a)

a = ['c', 'b', 'a']

a.sort()
print(a)