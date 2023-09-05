class Money(object):
    def __init__(self):
        self.__money = 0

    @property  # 相当于property的名字就是money
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        # isinstance不是必须
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")
        # 先写get，后写set，只写方法名字


m = Money()
m.money = 200  # 自动判断用哪个方法
print(m.money)
