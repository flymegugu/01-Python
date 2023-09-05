# 当调用的属性或者方法不存在的时候，会返回这个方法的定义信息
class test(object):
    def __getattr__(self, key):
        # print("hello")  # print("这个key：{}不存在".format(key))
        print("这个key：%s不存在" % key)  # print("这个key：{}不存在".format(key))
        return "haha"


t = test()
# t.a
print(t.a)
