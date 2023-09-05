# conding:utf-8
class tools(object):
    def work(self):
        return 'tools work'

    def car(self):
        return "car will run"


class food(object):
    def work(self):
        return "food work"

    def cake(self):
        return "i like cake"


class Person(tools, food):  # 父类的前后位置影响调用父类中方法的前后顺序
    pass


if __name__ == "__main__":
    p = Person()
    p_car = p.car()
    p_cake = p.cake()
    p_work = p.work()

    print(p_car)
    print(p_cake)
    print(p_work)
