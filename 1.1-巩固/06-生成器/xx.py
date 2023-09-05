'''
Author: [MaxGu]
Date: 2023-04-26 23:42:53
LastEditors: [MaxGu]
LastEditTime: 2023-04-28 13:14:29
Description:
'''


def func():
    print(111)
    v1 = yield 1
    print(v1)
    print(222)
    v2 = yield 2
    print(v2)
    print(333)
    v3 = yield 3
    print(v3)
    print(4444)


data = func()
print(data)
n1 = data.send(None)  # 等价 next
print(n1)

n2 = data.send(777)
print(n2)
n3 = data.send(None)
print(n3)
