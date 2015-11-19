__author__ = 'milton'
#coding=utf-8
import logging
logging.basicConfig(level=logging.INFO)
import pdb


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

# print(foo('0'))


def foo1(s):
    n = int(s)
    logging.info('n = %d' % n)
    return 10 / n

print(foo1('0'))