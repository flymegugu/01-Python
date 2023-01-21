class Person():
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge

    def eat(self):  # self表示使用这p1这个对象
        print("%s is eating" % self.name)


p1 = Person("tom", 20)
p1.eat()
