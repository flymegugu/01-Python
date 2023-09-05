'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-02-01 18:29:06
Description:
'''


def foo():
    print("foo")


def foo(x): return x+1  # foo=lambda x:x+1


a = foo(2)
print(a)
