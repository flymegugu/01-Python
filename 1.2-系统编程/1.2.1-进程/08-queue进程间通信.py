# 这个Queue队列模块只适用于Process方式创建的多进程数据交换
# 而Manager队列模块适用于Pool方式创建得进程池之间得数据交换
from multiprocessing import Process, Queue
import os
import time
import random


def write(q):
    for values in ['A', 'B', 'C']:
        print("put %s to queue.." % values)
        q.put(values)
        time.sleep(random.random())


def read(q):
    while True:
        if not q.empty():
            values = q.get(True)
            print("get %s from queue" % values)
            time.sleep(random.random())
        else:
            break


if __name__ == "__main__":
    # 父进程创建queue，并传给各个子进程
    q = Queue()
    # pw和pr分别开启了两个进程，对于这个操作来说，我们需要使用join来进行阻塞，否则会先执行主进程得print操作
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程
    pw.start()
    pw.join()
    # 启动子进程
    pr.start()
    pr.join()
    print(" ")
    print("所有数据都写入并且读完")
