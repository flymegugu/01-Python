'''
Author: [MaxGu]
Date: 2023-03-05 00:20:35
LastEditors: [MaxGu]
LastEditTime: 2023-03-05 00:26:18
Description:
'''
def counter():
    t1 = [0]
    def add_one():
        t1[0] += 1
        return t1[0]
    return add_one
num = counter()
print(num)