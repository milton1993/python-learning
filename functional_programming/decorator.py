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


def log3(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'begin call %s()' % func.__name__
        returnValue = func(*args, **kw)
        print 'end call %s()' % func.__name__
        return returnValue
    return wrapper


@log3
def now3():
    print '2015-11-16'

now3()
print(now3.__name__)


def log4(p):
    if p and isinstance(p, str):
        def decorator(f):
            @functools.wraps(f)
            def wrapper(*args, **kw):
                print '%s %s()' % (p, f.__name__)
                return f(*args, **kw)
            return wrapper
        return decorator
    else:
        def wrapper(*args, **kw):
            print 'call %s()' % p.__name__
            return p(*args, **kw)
        return wrapper


@log4
def now4():
    print '2015-11-16'

now4()


@log4('execute')
def now5():
    print '2015-11-16'

now5()