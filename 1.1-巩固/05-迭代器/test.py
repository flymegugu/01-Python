'''
Author: [MaxGu]
Date: 2023-04-14 16:44:30
LastEditors: [MaxGu]
LastEditTime: 2023-04-15 00:18:27
Description
'''


class A:
    """A 实现了迭代器协议 它的实例就是一个迭代器"""

    def __init__(self, n):
        self.idx = 0
        self.n = n

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        if self.idx < self.n:
            val = self.idx
            self.idx += 1

            return val
        else:
            raise StopIteration()


# 迭代元素
a = A(3)
for i in a:
    print(i)
