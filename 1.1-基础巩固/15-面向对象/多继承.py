class Base(object):
    def test(self):
        print("base")


class test1(Base):
    def test1(self):
        print("test1")


class test2(Base):
    def test2(self):
        print("test2")


class test3(test1, test2):
    pass


a = test3()

print(test3.__mro__)  # 可以查看方法搜索优先顺序
# (<class '__main__.test3'>, <class '__main__.test1'>, <class '__main__.test2'>, <class '__main__.Base'>, <class 'object'>)
