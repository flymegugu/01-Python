'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-02-28 14:17:17
'''
class haha(Exception):
    def __init__(self, message):
        super().__init__(message)


i = input("输入数值：")
n = 9899
try:
    result = n / int(i)
    print(result)
    print('{0},{1},{2}'.format(n, i, result))
except(ZeroDivisionError, ValueError) as e:
    # print("异常内容：{}".format(e))
    raise haha("这是个搞笑")
finally:
    print("释放资源")
