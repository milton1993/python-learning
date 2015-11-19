__author__ = 'milton'
#coding=utf-8


def fn(self, name='world'):
    print 'Hello, %s.' % name

Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
h.hello('Milton')


class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value : self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list):
    __metaclass__ = ListMetaClass

ML = MyList()
ML.add(1)
print(ML)


class Static(object):
    name = 'aaa'

s = Static()
print(s.name)
print(Static.name)
s.name = 'bbb'
print(s.name)
print(Static.name)
del s.name
print(s.name)
print(Static.name)