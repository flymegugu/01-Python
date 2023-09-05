'''
Author: [MaxGu]
Date: 2023-04-25 09:36:29
LastEditors: [MaxGu]
LastEditTime: 2023-04-25 09:36:30
Description:
'''


def log_time(func):  # 此函数的作用时接受被修饰的函数的引用test，然后被内部函数使用
    def make_decorater():
        print('现在开始装饰')
        func()
        print('现在结束装饰')
    return make_decorater  # log_time()被调用后，运行此函数返回make_decorater()函数的引用make_decorater


@log_time  # 此行代码等同于，test=log_time(test)=make_decorater
def test():
    print('我是被装饰的函数')


test()  # test()=make_decorater()
