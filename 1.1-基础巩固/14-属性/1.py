class test(object):
    @property
    def with_property(self):
        return 15

    def without_property(self):
        return 14


t = test()
print(t.with_property)  # 加了@property后，可以用调用属性的形式来调用方法,后面不需要加（）。
print(t.without_property())  # 没有加@property , 必须使用正常的调用方法的形式，即在后面加()
