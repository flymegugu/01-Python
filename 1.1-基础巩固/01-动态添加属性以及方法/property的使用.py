'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-01-22 22:18:20
Description:
'''
class Test(object):
    def __init__(self) -> None:
        super().__init__()
        self.__num = 100

    def getNum(self):
        return self.__num

    def setNum(self, newNum):
        self.__num = newNum
    # 通过property方法进行绑定
    num = property(getNum, setNum)


t = Test()
t.num = 400
print(t.getNum()) // TODO 随便写的