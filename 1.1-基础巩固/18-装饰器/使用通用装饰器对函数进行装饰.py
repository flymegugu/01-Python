def func(functionName):
    def func_in(*args, **kwargs):
        print("--输入日志--")
        ret = functionName(*args, **kwargs)
        return ret
    return func_in


@func
def test():
    print("--test--")
    return "test"


@func
def test2():
    print("--test2--")


@func
def test3(a):
    print("--test3--a=%d" % a)


ret = test()
print("test return value is %s" % ret)
a = test2()
# a 指向的这个函数没有返回值，所以为 None
print("test2 return value is %s" % a)

test3(11)
