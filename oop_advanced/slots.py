__author__ = 'milton'
# coding=utf-8
from types import MethodType


class Student(object):
    __slots__ = ('name', 'age', 'set_age')  # 限制允许对象绑定的属性名


s = Student()
s.name = 'Michael'
print s.name

# s.xxx = '123'


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s, Student)
s.set_age(25)
print s.age

s2 = Student()
# s2.set_age(12)
# print(s2.age)


Student.set_age = MethodType(set_age, None, Student)
s2.set_age(12)
print(s2.age)


# __slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的;
# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。