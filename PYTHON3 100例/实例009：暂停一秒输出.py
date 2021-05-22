import time
for i in range(4):
    # 通过[-1:]
    print(str(int(time.time()))[-1:])
    time.sleep(1)
