# 对于fork创建的子进程，主进程结束了，子进程该跑还跑，但是
# 对于process创建的子进程来说，主进程必须要等到子进程执行完毕后才会退出。
from multiprocessing import Process
import time


def test():
    for i in range(5):
        print("--test--")
        time.sleep(1)


if __name__ == '__main__':
    p = Process(target=test)
    p.start()
    p.join()  # join语句起到阻塞作用，必须等到子进程结束后，print("hello")才会执行
    print("hello")
