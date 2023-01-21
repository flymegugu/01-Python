class A():
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test1(self):
        print("---test1---")

    def __test2(self):
        print("---test2---")

    def test3(self):
        self.__test2()

# super调用父类的方法，可以通过公有方法包裹私有方法的方式，给第三方提供服务，但是通过公有方法的方法名必须是父类存在的公有方法名，
# 你不能自己在自己类中自定义去调用，因为父类知道你是假冒的


class B(A):
    pass
    # def __init__(self):
    #     super().__init__()  # 显示继承父类的init后才能引用父类变量
    #     super().test1()
    #     super().test3()
    #     # super().num1


b = B()
print(b.num1)
# print(b.__num2)
# 如果继承后不显式写init初始化函数的化，那么自动继承父类的init方法，但是如果在子类中写了init那么就要写实的引用父类的init，才能使用父类的方法
