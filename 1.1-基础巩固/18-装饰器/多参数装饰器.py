def func(functionName):
    print("--func1--")

    def func_in(*args, **kwargs):
        print("--func_in--1--")
        functionName(*args, **kwargs)
        print("--fnnc_in_-2--")
    print("--func_2--")
    return func_in


@func
def test(a, b, c):
    print("--test-a=%d,b=%d,c=%d" % (a, b, c))


test(11, 22, 33)
