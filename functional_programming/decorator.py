__author__ = 'milton'
#coding=utf-8
import functools


def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log   # @log相当与执行了now = log(now)
def now():
    print '2015-11-13'

now()


def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log1('execute')
def now1():
    print '2015-11-13'

now1()
print(now1.__name__) # wrapper


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator


@log2('run')
def now2():
    print '2015-11-13'

now2()
print(now2.__name__)