def func(functionName):
    print("--func--1")

    def func_in():
        print("--func_in--1--")
        ret = functionName()  # 此处调用test()后返回值给ret
        print("--func_in--2--")
        return ret
    return func_in


@func
def test():
    print("--test--")
    return "haha"


# test()
ret = test()
print("test return value is %s" % ret)
