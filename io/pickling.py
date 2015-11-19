__author__ = 'milton'
#coding=utf-8

try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='bob', age=20, score=88)
print pickle.dumps(d)

f = open('a.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('a.txt', 'rb')
d = pickle.load(f)
f.close()
print d