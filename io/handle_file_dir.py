__author__ = 'milton'
#coding=utf-8

import os
print os.name

print os.uname()
print os.environ
print os.getenv('JAVA_HOME')
print os.path.abspath('.')
# os.mkdir(os.path.join('.', 'testdir'))
# os.rmdir(os.path.join('.', 'testdir'))
print os.path.split('/home/milton/downloads/aaa.txt')
print os.path.splitext('/home/milton/downloads/aaa.txt')

# os.rename('/home/milton/downloads/aaa.txt', 'bbb.txt')
# os.remove('bbb.txt')

# import shutil
# shutil.copyfile('/home/milton/todo', './todo')

# os.remove('todo')

print [x for x in os.listdir('/home/milton/') if os.path.isfile(os.path.join('/home/milton', x))]