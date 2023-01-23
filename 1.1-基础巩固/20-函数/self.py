'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-01-23 20:49:16
Description:
'''
class Dog:
    def __init__(self,name,age,sex="女孩"):
        self.name = name
        self.age = age
        self.sex = sex
    def run(self):
        print("{0}岁的狗狗 {1} is running".format(self.age,self.name))
    def speak(self,sound):
        print("{0} is speak {1}".format(self.name,sound))

dog = Dog('球球',2)
dog.run()
dog.speak('旺旺旺')