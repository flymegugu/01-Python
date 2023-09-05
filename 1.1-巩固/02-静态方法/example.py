'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-04-23 23:54:46
Description:
'''
# 类属性可以给这个类中的所有方法所共享，


class Game(object):
    num = 0
# 实例对象的方法需要加self，可自定义名字，但没必要

    def __init__(self):
        self.name = "laowang"
# 类方法需要加cls，可自定义名字但是没必要

    @classmethod  # 类方法，用于修改类属性的东西,当调用这个类方法时候才会修改
    def add_num(cls):
        cls.num = 100

    @staticmethod
    # 静态方法和实例方法和类方法没啥关系，括号内可加可不加参数
    def print_menu():
        print("--1--")
        print("--ok--")


game = Game()
Game.add_num()  # 可以通过类名调用类方法
game.add_num()  # 可以通过实例化对象调用类方法
print(Game.num)

Game.print_menu()  # 通过类调用静态方法
game.print_menu()  # 通过实例化对象调用静态方法
