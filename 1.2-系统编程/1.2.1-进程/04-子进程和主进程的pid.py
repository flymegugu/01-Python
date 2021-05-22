import os
ret = os.fork()
print(ret)
if ret > 0:
    while True:
        print("---父进程--%d-" % os.getpid())
else:
    while True:
        print("---子进程--%d-%d-" % (os.getpid(), os.getppid()))
