__author__ = 'milton'

d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])

print(len(d))

d['d'] = 4
print(len(d))

print('e' in d)


print(d.get('f'))
print(d.get('f', -1))

d.pop('b')
print(d)

#dict内部存放的顺序和key放入的顺序是没有关系的
#dict的key必须是不可变对象