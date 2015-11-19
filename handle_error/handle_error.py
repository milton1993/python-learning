__author__ = 'milton'
#coding=utf-8
import logging

try:
    print 'try...'
    r = 10 / 2
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
else:
    print 'no error!'
finally:
    print 'finnally...'
print 'END'


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()