__author__ = 'milton'
#coding=utf-8


class Student(object):
    __slots__ = ('__name', '__sex', '__score', '__age')

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.__name

    __repr__ = __str__

print Student('Mike')


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration()
        return self.a

for n in Fib():
    print n


class Fib1(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib1()
print(f[0])

print(f[100])

print(f[0:5])


class List(object):
    def __init__(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size <= 0:
            size = 16
        self.__L = []
        self.__length = 0
        self.__size = size

    def __len__(self):
        return self.__length

    def __getitem__(self, n):
        if isinstance(n, int):
            return self.__L[n]
        if isinstance(n, slice):
            return self.__L[slice.start: slice.stop: slice.step]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('key must be an integer')
        if key >= self.__size:
            self.__size *= 2
        self.__L.insert(key, value)
        if key >= self.__length:
            self.__length = key + 1

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('key must be an integer')
        if key >= self.__length:
            raise IndexError('index out of range: %d' % key)
        i = key
        while i < self.__length - 1:
            self.__L[i] = self.__L[i+1]
            i += 1
        self.__L.pop()
        self.__length -= 1

    def add(self, value):
        if self.__length >= self.__size:
            self.__size *= 2
        self.__L.append(value)
        self.__length += 1

    delete = __delitem__

    def __str__(self):
        return 'List object: %s' % self.__L

    __repr__ = __str__

l = List(1)
l.add('a')
l.add('b')
l.add('c')
l.add('d')
l.add('e')
print(l)

# l.delete(5)
l.delete(2)
print(l)


class Call(object):
    def __init__(self, name):
        self.__name = name

    def __call__(self, *args, **kwargs):
        print("My name is %s" % self.__name)

c = Call('Milton')
c()