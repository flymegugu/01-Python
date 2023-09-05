from multiprocessing import Pool
import os
import time
import random


def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop-t_start))


po = Pool(3)
for i in range(0, 10):
    po.apply_async(worker, (i,))
print("--start--")
po.close()  # 关闭进程池，关闭后po不再接收新的请求
po.join()  # 等待po中所有子进程执行完毕，必须放在close()之后
print("--end--")
# 执行结果如下：
# --start--
# 0开始执行，进程号为27428
# 1开始执行，进程号为27429
# 2开始执行，进程号为27430
# 1 执行完毕，耗时0.10
# 3开始执行，进程号为27429
# 0 执行完毕，耗时0.30
# 4开始执行，进程号为27428
# 2 执行完毕，耗时0.89
# 5开始执行，进程号为27430
# 3 执行完毕，耗时1.35
# 6开始执行，进程号为27429
# 4 执行完毕，耗时1.41
# 7开始执行，进程号为27428
# 6 执行完毕，耗时0.45
# 8开始执行，进程号为27429
# 5 执行完毕，耗时1.40
# 9开始执行，进程号为27430
# 8 执行完毕，耗时0.85
# 7 执行完毕，耗时1.61
# 9 执行完毕，耗时1.49
# --end--
