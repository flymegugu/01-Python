class Dog():
    def __del__(self):
        print("已经呗干掉")


# 程序结束后 ，那么程序就会释放内存，所以就是执行del方法，
a = Dog()
b = a

del a
# del b
print("============")
