# 拦截当前类中不存在的属性与值
class test(object):
    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__[key] = value


t = test()
t.name = "tom"
print(t.name)
