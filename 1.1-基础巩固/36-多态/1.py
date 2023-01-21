# coding:utf-8
class tomFather(object):
    def talk(self):
        print("tom爸爸的一句话")


class tomBrother(tomFather):
    def run(self):
        print("tom哥哥在奔跑")

    def talk(self):
        print("tom哥哥在说话")


if __name__ == '__main__':
    tom_brother = tomBrother()
    tom_brother.run()
    tom_brother.talk()
    tom_father = tomFather()
    tom_father.talk()
