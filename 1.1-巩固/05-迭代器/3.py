print("--示例1--")
iter_obj = iter((1, 2, 3))


def test(iter_obj):
    print("---")
    # return next(iter_obj) #此处搭配11行的print
    # 此处搭配10行的test（iter_obj）,要不你return后print，要不你直接print，然后通过test(iter_obj) 进行调用
    print(next(iter_obj))


test(iter_obj)
# print(test(iter_obj))
print("--end--")
########################################################################################################################
print("--示例2--")
#iter_obj = iter((1, 2, 3))
# def test(iter_obj):
#    try:
#        return next(iter_obj)   # next操作会有一个返回值，需要return取过来，或者直接print（next（iter_obj）输出
#        print(next(iter_obj))
#    except StopIteration:
#        # return None
#        print("kkk")
#
#
# test(iter_obj)
# test(iter_obj)
# test(iter_obj)
# test(iter_obj)
