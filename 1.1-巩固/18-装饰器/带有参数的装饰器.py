from time import ctime, sleep


def timefun_arg(pre="hello"):
    def timefun(func):
        def wrappendfunc():
            print("%s called at %s %s " % (func.__name__, ctime(), pre))
            return func()
        return wrappendfunc
    return timefun


@timefun_arg("itcast")
def foo():
    print("i am foo")


@timefun_arg("python")
def too():
    print("i am too")


@timefun_arg()
def test():
    print("i am test")


foo()
sleep(1)
too()
sleep(1)
test()
