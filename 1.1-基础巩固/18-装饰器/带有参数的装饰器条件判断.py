def func_arg(arg):
    def func(functionName):
        def func_in():
            print("--记录日志-arg=%s" % arg)
            if arg == "heihei":
                functionName()
                functionName()
            else:
                functionName()
        return func_in
    return func


# 带有参数的装饰器能够起到在运行时，有不同的功能
@func_arg("heihei")
def test():
    print("--test--")


@func_arg("haha")
def test2():
    print("--test2--")


test()
test2()
