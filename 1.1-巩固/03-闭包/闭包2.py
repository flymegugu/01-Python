'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-03-09 23:05:40
Description:
'''


def test1(num1):
    def test2(num2):
        print(num1+num2)
    return test2


t = test1(22)
t(4)
