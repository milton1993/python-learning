__author__ = 'milton'
#coding=utf-8


class Student(object):  # 括号中表示继承关系
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

a = Student('A', 20)
# print(a.__name)
print(a.get_name())
print(a._Student__name)  # 私有变量其实是被python解释器修改了名字