__author__ = 'milton'
#coding=utf-8


class Student(object):  # 括号中表示继承关系
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

stu1 = Student('a', 13)
stu2 = Student('b', 20)

print(stu1.name)
print(stu2.score)

stu1.print_score()
print(stu2.get_grade())