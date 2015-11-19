__author__ = 'milton'
#coding=utf-8


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must be betweent 0 and 100')
        self._score = value

s = Student()
s.score = 60
print(s.score)

# s.score = 9999


# 定义只读属性
class Person(object):
    @property
    def birth(self):
        return self.__birth

    @birth.setter
    def birth(self, value):
        self.__birth = value

    @property
    def age(self):
        return 2015 - self.__birth

p = Person()
p.birth = 1993
print(p.birth)
print(p.age)
# p.age = 22