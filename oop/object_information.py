__author__ = 'milton'
#coding=utf-8
import class_instance
import types

print(type(123))
print(type(None))
print(type(abs))

a = class_instance.Student('a', 12)

print(type(a))

print(type('abc') == types.StringType)
print(type(u'abc') == types.UnicodeType)  # 使用isinstance()
print(type(int) == type(str) == types.TypeType)


print(dir(a))  # dir可以获得一个对象的所有属性和方法

#在len()函数内部，它自动去调用该对象的__len__()方法

print(hasattr(a, 'name'))
print(hasattr(a, 'namexxx'))
setattr(a, 'xxx', 13)
print(hasattr(a, 'xxx'))
print(getattr(a, 'xxx'))
print(a.xxx)
setattr(a, '__yyy', 13)
print(hasattr(a, '__yyy'))
print(getattr(a, '__yyy'))
print(a.__yyy)
print(getattr(a, 'aaa', 4))