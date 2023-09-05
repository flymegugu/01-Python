# -*- coding:utf-8 -*-

class A(object):
    _test = "heihei"

    def __init__(self):  # 系统定义方法
        self.string = 'A string'
        self._string = 'A _string'
        self.__string = 'A __string'  # 私有变量

    def fun(self):
        return self.string + ' fun-A'

    def _fun(self):
        return self._string+'  _fun-A'

    def __fun(self):  # 私有方法
        return self.__string+' __fun-A'

    def for__fun(self):  # 内部调用私有方法
        return self.__fun()


class B(A):

    def __init__(self):  # 系统定义方法
        self.string = 'B string'


b = B()
print(b.fun())
print(b._test)
