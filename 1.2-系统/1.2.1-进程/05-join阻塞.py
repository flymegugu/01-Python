'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2022-08-16 22:28:40
Description:
'''
# coding:utf-8
from multiprocessing import Process
import os


def run_proc(name):
    print("子进程运行中，name=%s,pid=%d.." % (name, os.getpid()))


if __name__ == "__main__":
    print("父进程%d." % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print("子进程将要执行")
    p.start()
    p.join()
    print("子进程已结束")
