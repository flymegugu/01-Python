'''
Author: [MaxGu]
Date: 2022-08-24 22:31:54
LastEditors: [MaxGu]
LastEditTime: 2023-01-20 12:49:34
Description:
'''


def pattern(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")

