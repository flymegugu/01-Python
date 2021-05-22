# 此例子init需要初始化1次
class Dog(object):
    __instance = None
    __init_flag = False
# 此处要穿两个参数，第一个为Dog类对象，第二个为name形参

    def __new__(cls, name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
# 通过添加if判断，此处init初始化一次，对象调用init则不会改变，上面是cls.__instance是应为开始没有对象
# 需要创建通过new创建对象，而这里是通过创建好的Dog类对象进行init初始化操作

    def __init__(self, name):
        if Dog.__init_flag == False:
            self.name = name
            # 设置为True则修改名字不会生效，因为不会执行self.name = name
            Dog.__init_flag = True


# 都是同一个对象的引用，所以id都一样
a = Dog("旺财")
print(id(a))
print(a.name)


b = Dog("哮天犬")
print(id(b))
print(b.name)
