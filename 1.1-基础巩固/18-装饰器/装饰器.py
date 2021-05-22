class Test(object):
    def __init__(self) -> None:
        super().__init__()
        self.__num = 100

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, newNum):
        self.__num = newNum


t = Test()
t.num = 4090
print(t.num)
