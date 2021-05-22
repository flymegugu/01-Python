class Test(object):
    def __init__(self, switch):
        self.switch = switch

    def calc(self, a, b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print("捕获已开启，信息如下：")
                print(result)
            else:
                # 我自己不捕获异常了，直接交给解释器，用默认的异常处理
                raise


a = Test(True)
a.calc(11, 0)
print("-----------------华丽分割线----------------")
# 此处更改为False
a.switch = False
a.calc(11, 0)
