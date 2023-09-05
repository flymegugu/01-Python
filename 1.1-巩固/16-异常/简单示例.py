# 一个位置捕获到异常，则此位置后的命令不会执行
try:
    # print(num)
    print("--1--")
    open("xxx.txt")
except NameError:
    print("捕获异常后的处理")
except Exception as log:
    print("捕获找不到文件异常")
    print("异常名字为%s" % (log))
else:
    print("没有异常才会执行")
finally:
    print("无论是否异常都会输出此内容")

print("--2--")
