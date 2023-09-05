class pay():
    def __sendmsg(self):
        print("你充值了")

    def passd(self, money):
        if money > 100:
            self.__sendmsg()
        else:
            print("不给过")


a = pay()
a.passd(1000)
