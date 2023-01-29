'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-01-27 13:06:31
Description:
'''
registry = []


def register(func):
    print("装饰器 register---running register(%s)" % func)
    registry.append(func)
    return func


@register
def f1():
    print('f1----running f1()')


@register
def f2():
    print('f2----running f2()')


def f3():
    print('f3----running f3()')


def main():
    print("running main()")
    print('registry->', registry)
    f1()
    f2()
    f3()
    print(registry)


if __name__ == "__main__":
    main()
