'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-03-10 13:23:10
Description:
'''
def test1(a, **kwargs):
    print(a)
    print(kwargs)
# **kwargs是将kwargs字典的每一个元素分别拿出来，一次还原成m=100，n=2,但是**kwargs不支持打印出来
#    print(**kwargs)
    test2(**kwargs)


def test2(m, n):
    print(m, n)


test1(1, m=100, n=2)
