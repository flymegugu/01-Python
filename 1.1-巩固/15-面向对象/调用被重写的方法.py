class Animal(object):
    def bark(self):
        print("wwwww")


class Dog(Animal):
    def bark(self):
        print("kkkk")
        Animal.bark(self)  # 这种方式调用父类方法要加self
        # super().bark()
        super(Dog, self).bark()


a = Dog()
a.bark()
