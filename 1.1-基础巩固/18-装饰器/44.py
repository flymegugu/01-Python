'''
Author: [MaxGu]
Date: 2023-01-29 22:38:15
LastEditors: [MaxGu]
LastEditTime: 2023-01-29 22:40:06
Description:
在part1中，从functools里面导出wraps函数，这个我们是在下面用来装饰函数的。
在part2中，我们将一个函数传f递进去,然后这个在part3中的wrapper函数中使用，wrapper会把这个结果输出来，然后calruntime把warpper这个函数对象输出来。
part3中的wrapper使用了args，kargs之类的，就是希望不要影响myrun函数使用参数，不然参数传递少了，myrun函数回很生气。
结束
'''
# part1
from functools import wraps
from datetime import datetime
from time import sleep

# part2


def calruntime(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # part3
        print(f"start run datetime: {datetime.now()}")
        value = f(*args, **kwargs)
        print(f"end run dateime: {datetime.now()}")

        return value

    return wrapper


# part4
@ calruntime
def myrun(a, b, c):
    sleep(2)
    return a + b + c


# part5
if __name__ == "__main__":
    # part6
    a = myrun(a=1, b=2, c=3)
    print(a)
