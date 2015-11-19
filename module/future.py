from __future__ import unicode_literals
from __future__ import division
__author__ = 'milton'
#coding=utf-8

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

print(10/3)
print(10.0/3)
print(10//3)