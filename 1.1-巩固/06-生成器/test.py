'''
Author: [MaxGu]
Date: 2023-04-24 16:37:57
LastEditors: [MaxGu]
LastEditTime: 2023-04-24 17:20:11
Description:
'''
def foo():
    print("start")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print(next(g))