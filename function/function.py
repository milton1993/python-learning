__author__ = 'milton'
# -*- coding=utf-8 -*-


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('type error')
    if x >= 0:
        return x
    else:
        return -x

#使a指向abs函数
a = my_abs
print(a(-1))

# print(a('A'))


#函数可以返回多个返回值
def two_return_value(x, y):
    return x, y


x, y = two_return_value(1, 2)
print(x)
print(y)

x = two_return_value(1, 2)
print(x)
#实际返回的是一个tuple

x, y = (1, 2)
print(x)
print(y)


#设置默认参数值
def power(number, times=2):
    if not isinstance(number, (int, float)):
        raise TypeError('number must be an integer or a float')
    if not isinstance(times, int):
        raise TypeError('times must be an integer')
    s = 1
    if times >= 0:
        while times > 0:
            times -= 1
            s *= number
    else:
        while times < 0:
            times += 1
            s = float(s) / number
    return s

print(power(5))

print(power(5, 3))

print(power(5, 0))

print(power(5, -3))


def enroll(name, gender, age=6, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('abc', 'F')
enroll('ddd', 'M', 18)
enroll('ccc', 'F', city='shanghai')


# def add_end(l=[]):
#     l.append('end')
#     return l
#


def add_end(l=None):
    if l is None:
        l = []
    l.append('end')
    return l

print(add_end())
print(add_end())
print(add_end())

#函数的默认参数必须指向不可变对象


#可变参数：自动组装成tuple
def calc(*numbers):
    result = 0
    for n in numbers:
        result += n * n
    return result

print(calc(1, 2))
print(calc(1, 2, 3))

nums = [2, 4, 5]
print(calc(nums[0], nums[1], nums[2]))
print(calc(*nums))


#关键字参数：自动组装成dict
def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)

person('a', 12)
person('a', 12, city='beijing', gender='M')
person('a', 12, city='beijing')

kw = {'city': 'beijing', 'gender': 'M'}
person('a', 12, city=kw['city'], gender=kw['gender'])
person('a', 12, **kw)

#参数定义的顺序必须是：必选参数、默认参数、可变参数、关键字参数


def func(a, b, c=0, *args, **kw):
    print("a:", a, "b:", b, "c:", c, "args:", args, "kw:", kw)

args = (1,2,3,4)
kw = {'x': 99}
func(*args, **kw)