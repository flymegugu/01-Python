# 两个装饰器：
def w1(func):
    print("---正在装饰1---")

    def inner1():
        print("---正在验证权限1---")
        func()
    return inner1


def w2(func):
    print("---正在装饰2---")

    def inner1():
        print("---正在验证权限2---")
        func()
    return inner1


@w1
@w2
def f1():
    print("---f1---")


f1()
