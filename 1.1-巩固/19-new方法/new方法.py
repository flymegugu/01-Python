class Dog(object):
    def __init__(self):
        print("----init方法----")

    def __del__(self):
        print("----del方法----")

    def __str__(self):
        print("----str方法----")
        return "对象描述信息"

    def __new__(cls):
        print(id(cls))
        print("----new方法----")


print(id(Dog))
dog = Dog()
