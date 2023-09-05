# 此程序需要在linux环境执行，因为Windows没有fork调用，上面的代码在Windows上无法运行
import os
import time
ret = os.fork()
if ret == 0:
    while True:
        print("111")
        time.sleep(1)
else:
    while True:
        print("222")
        time.sleep(1)
