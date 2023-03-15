'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-03-05 00:32:26
Description:
'''


def counter():
    cnt = [0]

    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one


num = counter()
num = counter()
print(num())
