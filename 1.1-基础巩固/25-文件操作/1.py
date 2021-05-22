# coding=utf-8
f = None
try:
    f = open(r'C:\Users\大G\Desktop\test\tesdt.txt')
    content = f.read()
    print(content)
except FileNotFoundError as e:
    print("文件不存在%s" % e)
except OSError as e:
    print("处理os异常")
finally:
    if f is not None:
        f.close()
        print("文件关闭")
