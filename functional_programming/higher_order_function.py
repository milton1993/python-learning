__author__ = 'milton'
#coding=utf-8


def add(x, y, f):
    return f(x) + f(y)

print(add(5, -11, abs))


#map/reduce
def fn(x, y):
    return 10 * x + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(fn, map(char2num, '12345')))  #实现string转换成数字


def first_upper(s):
    result = ''
    for x, ch in enumerate(s):
        if x == 0:
            result += ch.upper()
        else:
            result += ch.lower()
    return result

print(map(first_upper, ['adam', 'aliCe', 'OK']))


def prod(List):
    return reduce(lambda x, y: x * y, List)

print(prod(range(1, 100)))


#filter函数
def is_odd(n):
    return n % 2 == 1

print(filter(is_odd, range(100)))


#sorted函数
L = [36, 5, 12, 9, 43]
print(sorted(L))


def reverse_cmp(x, y):
    if x > y:
        return -1
    elif x < y:
        return 1
    return 0

print(sorted(L, reverse_cmp))

S = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(S))


def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print(sorted(S, cmp_ignore_case))