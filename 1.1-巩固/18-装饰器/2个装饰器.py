'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-01-29 12:38:17
Description:
'''


def w1(func):
    print("---------------w1")

    def inner1():
        print("------------inner1")
        func()
    return inner1
def w2(func):
    print("-------------------w2")
    def inner2():
        print("---------------inner2")
        func()
    return inner2

@w1
@w2
def f1():
    print("tttttttttttttttttt")


f1()
