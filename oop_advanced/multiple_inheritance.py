__author__ = 'milton'
#coding=utf-8


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable(object):

    def run(self):
        print('running...')


class Flyable(object):
    def fly(self):
        print('flying...')


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird, Flyable):
    pass


class Hen(Bird, Runnable):
    pass