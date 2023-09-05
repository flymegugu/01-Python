'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-04-21 13:18:10
Description:
'''
def test(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
#    print(args)
    print(*args)  # 加*表示拆包
    print(kwargs)  # 这里得kwargs不能加**，拆不了


A = (44, 55, 66)
B = {"name": "laowang", "age": 16}
# test(11, 22, 33, *A, B)#只有当**B得时候才会把B从元组里面踢出去，放到该放得位置
test(11, 22, 3322, *A, **B)  # 只有当**B得时候才会把B从元组里面踢出去，放到该放得位置
