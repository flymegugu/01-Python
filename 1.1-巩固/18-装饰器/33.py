'''
Author: [MaxGu]
Date: 2023-01-29 22:03:30
LastEditors: [MaxGu]
LastEditTime: 2023-01-29 22:34:27
Description:装饰带有不定长参数的函数
'''


def logging(fn):
    def inner(*args, **kwargs):
        print("努力计算")
        fn(*args, **kwargs)
    return inner

#sum_num = logging(sum_num)
@logging
def sum_num(*args, **kwargs):
    result = 0
    for value in args:
        result += value
    for value in kwargs.values():
        result += value
    print(result)


sum_num(1, 2, a=10)
