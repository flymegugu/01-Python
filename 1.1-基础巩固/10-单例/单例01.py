# object代表Dog是一个类
class Dog(object):
    # 类的私有属性instance
    __instance = None

# 复写父类的new方法，不复写那么直接用父类的new方法，复写就是进行改进和判断
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            print(cls)
            print(cls.__instance)
            return cls.__instance
        else:
            print(cls)
            print(cls.__instance)
            return cls.__instance


a = Dog()
print(id(a))
b = Dog()
print(id(b))
