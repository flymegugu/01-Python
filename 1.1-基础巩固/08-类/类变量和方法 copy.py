# -*- coding: UTF-8 -*-

class A(object):
    bar = 1
# 带有self的必须实例化才可以使用

    def func1(self):
        print('foo')

    @classmethod
    def func2(cls):
        print('func2')
        print(cls)
        print(cls())
        print(cls.bar)
        cls().func1()   # 调用 foo 方法


A.func2()               # 不需要实例化
