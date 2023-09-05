'''
Author: [MaxGu]
Date: 2023-04-25 12:59:22
LastEditors: [MaxGu]
LastEditTime: 2023-04-25 13:11:34
Description:
'''


def log_time(func):
    def make_decorater(*args, **kwargs):  # 接受调用语句的实参，在下面传递给被装饰函数（原函数）
        print('现在开始装饰')
        test_func = func(*args, **kwargs)  # 如果在这里return，则下面的代码无法执行，所以引用并在下面返回
        print('现在结束装饰')
        # 因为被装饰函数里有return，所以需要给调用语句（test（2））一个返回，又因为test_func = func(*args,**kwargs)已经调用了被装饰函数，这里就不用带（）调用了，区别在于运行顺序的不同。
        return test_func
    return make_decorater


@log_time  #test=log_time(test)=make_decorater
def test(num):
    print('我是被装饰的函数')
    return num+1


a = test(2)  # a= test(2)=make_decorater(2)=test_func
print(a)
