'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-03-05 00:33:10
Description:
'''


def line_conf(a, b):
    def line(x):
        return a*x + b
    return line


line1 = line_conf(1, 1)
line2 = line_conf(4, 6)
print(line1(5))
print(line2(5))
