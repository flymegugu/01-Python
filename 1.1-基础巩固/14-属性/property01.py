class Money(object):
    def __init__(self):
        self.__money = 0

    def getMoney(self):
        return self.__money

    def setMoney(self, value):
        # isinstance不是必须
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")
        # 先写get，后写set，只写方法名字
    money = property(getMoney, setMoney)


m = Money()
m.money = 200
print(m.money)
