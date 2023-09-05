# 这个Queue队列模块只适用于Process方式创建的多进程数据交换
# 而Manager队列模块适用于Pool方式创建得进程池之间得数据交换
from multiprocessing import Manager, Pool
import os
import time
import random


def reader(q):
    print("reader启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到得消息：%s" % q.get(True))


def writer(q):
    print("writer启动(%s),父进程为(%s)" % (os.getpid(), os.getppid()))
    for i in "dongGe":
        q.put(i)


if __name__ == "__main__":
    q = Manager().Queue()  # 使用manager中得queue进行队列初始化
    po = Pool()
    po.apply(writer, (q,))
    po.apply(reader, (q,))
    po.close()
    po.join()
    print("(%s) END" % os.getpid())
