from multiprocessing import Pool
import os
import time
import random


def worker(num):
    for j in range(5):  # 这里单个进程执行的次数
        print("worker 的 j 的值 为: %d ，目前进程号为：%d ，目前获取到的 i 的值为：%d" %
              (j, os.getpid(), num))
        time.sleep(1)


if __name__ == "__main__":
    pool = Pool(3)

    for i in range(4):
        print("---%d---" % i)
        pool.apply_async(worker, (i,))
    pool.close()
    pool.join()
    print("hello")
