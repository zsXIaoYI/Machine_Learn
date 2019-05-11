# -*- coding: utf-8 -*-
# __author__ = 'zs'
# 2019/4/13 下午8:37


print(111)


# self:和Java中的this类似
# 1、__init__ 类似于Java的构造方法
# 2、__str__ 类似于Javat的toString()方法


class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name


print(Student('Jack'))  # Student object (name: Jack)


# 斐波那契数列
# 如果一个类想被用于for循环, 类似list或tuple, 就必须实现一个__iter__()方法
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration
        return self.a


for n in Fib():
    print(n)


class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            print(isinstance(n, slice))
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


# f = Fib2()
# print(f[0:5])

f1 = Fib2()
print(f1[5])
