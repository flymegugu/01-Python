class Dog:
    def __init__(self, name, age, sex="hello"):
        self.name = name
        self.__age = age

    def run(self):
        print("{} is run".format(self.name))

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


dog = Dog('球球', 2)
print("狗狗年龄:{}".format(dog.age))
dog.age = 3
print("修改后年龄为:{}".format(dog.age))
