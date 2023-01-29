'''
Author: [MaxGu]
Date: 2023-01-29 21:37:04
LastEditors: [MaxGu]
LastEditTime: 2023-01-29 21:46:41
Description:装饰带有返回值的函数
'''


def logging(fn):
    def inner(num1, num2):
        print("正在计算")
        result = fn(num1, num2)
        return result
    return inner


@logging
def sum_num(a, b):
    result = a + b
    return result


result = sum_num(1, 2)
print(result)
