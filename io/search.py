__author__ = 'milton'
#coding=utf-8
import sys
import os
reg = sys.argv[1]


def search(s):
    for x in os.listdir('.'):
        if x.__contains__(s):
            print x

search(reg)