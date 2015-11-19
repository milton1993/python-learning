__author__ = 'milton'
# coding=utf-8
'a test module'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello World!'
    elif len(args) == 2:
        print 'Hello, %s' % args[1]
    else:
        print 'too many arguments!'

# 当我们在命令行运行当前模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败
if __name__ == '__main__':
    test()