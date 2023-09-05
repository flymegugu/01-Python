'''
Author: [MaxGu]
Date: 2023-04-25 00:19:01
LastEditors: [MaxGu]
LastEditTime: 2023-04-25 09:35:26
Description:;'

'''
import random
import time


def time_check(func):
    def inner():
        start = time.time()
        for i in func(*args, **kwargs):
            print(i)
        end = time.time()
        print('用时:{}秒'.format(end-start))
    return inner


@time_check
def test(max_num):
    counter = 0
    while counter < max_num:
        yield random.randint(1000, 9999)
        counter += 1


test(10000)
########################################
# def func():
#    print(123)
#    yield 4
#    print(456)
#    yield 5
#    print(789)
#
#v1 = func()
# print(v1)
# for i in v1:
#    print(i)


# @time_check
# def test1():
#    data_list = []
#    for i in range(100000):
#        random.randint(1000, 9999)
#        data_list.append(i)
#    print(data_list)
#
