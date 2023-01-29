'''
Author: [MaxGu]
Date: 2023-01-29 16:08:21
LastEditors: [MaxGu]
LastEditTime: 2023-01-29 16:20:03
Description:带有参数得函数
'''


def logging(fn):
    def inner(num1, num2):
        print("努力计算中")
        fn(num1, num2)
    return inner


@logging
def sum_num(a, b):
    result = a + b
    print(result)


sum_num(1, 2)
