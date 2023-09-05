class Animal(object):
    def __init__(self):
        self.name = "我是父类"

    def A(self):
        print("父类的A方法")


class Panda(Animal):
    def __init__(self):
        super().__init__()
        self.myname = "pandar"

    def A(self):
        print("子类A的方法")

    def B(self):
        self.A()
        super().A()


if __name__ == "__main__":
    panda = Panda()
    panda.B()
