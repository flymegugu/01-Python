'''
Author: [MaxGu]
Date: 2022-11-19 12:39:33
LastEditors: [MaxGu]
LastEditTime: 2022-11-19 22:44:21
Description:
'''
w = int(input("xxx"))
list = []


def list_1(n):
    if n >= 3:
        res = list_1(n-1) + list_1(n-2)
    else:
        res = 1
    for i in range(0, w):
        list_res.append(list_1(i+1))


print(list_res)
