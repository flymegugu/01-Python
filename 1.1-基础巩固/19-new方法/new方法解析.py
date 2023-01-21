# object可写可不写，默认是object，默认继承父类的new方法创建对象

class Dog(object):
    def __init__(self):
        print("--init方法--")

    def __del__(self):
        print("--del方法--")

    def __str__(self):
        print("--str方法--")
        return "对象的描述信息"

    def __new__(cls):  # cls此时是Dog指向的那个类对象
        # print("1---cls-id", id(cls))
        print("--new方法--")
        # 返回通过父类object对象的new()方法创建对象，通过new方法将Dog类的对象(类也是一个对象)创建出来，
        return object.__new__(cls)


# 此处的Dog是 class Dog()这个类的对象
print("2--id-Dog", id(Dog))
# 实例化一个Dog对象
xtq = Dog()
