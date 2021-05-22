# 此例子init需要初始化两次
class Dog(object):
    __instance = None
# 此处要穿两个参数，第一个为Dog类对象，第二个为name形参

    def __new__(cls, name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, name):
        self.name = name


# 都是同一个对象的引用，所以id都一样
a = Dog("旺财")
print(id(a))
print(a.name)


b = Dog("哮天犬")
print(id(b))
print(b.name)
