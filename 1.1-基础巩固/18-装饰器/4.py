'''
Author: [MaxGu]
Date: 2023-01-28 20:38:32
LastEditors: [MaxGu]
LastEditTime: 2023-01-29 13:24:26
Description:
'''


def func_arg(arg):
    def func(funcName):
        # 此处为通用装饰器，既可以接收参数也可以接收返回值
        def func_in(*args, **kwargs):
            if arg == "hello":
                ret = funcName(*args, **kwargs)  # 被装饰的函数传值能接收，有return也可以接收
                return ret
            else:
                print("is not hello")
        return func_in
    return func


@func_arg("hello")
def test(v1):
    print("hello--%s" % v1)
    return "v1"


k = test("abc")
print("the return value is %s" % k)
