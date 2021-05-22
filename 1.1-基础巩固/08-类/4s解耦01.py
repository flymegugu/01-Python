# coding = utf-8
# 4s店例子,此类object 有order函数,函数一般有self,函数又返回一个方法调用select_car_by_type
class CarStore(object):
    # 创建完对象立刻调用init函数
    def __init__(self):
        self.factory = Factory()

    def order(self, car_type):
        return self.factory.select_car_by_type(car_type)


class Factory(object):
    # 有self的一般为函数,没有的一般为方法
    def select_car_by_type(car_type):
        if car_type == "suonata":
            return Suonata(Car)
        elif car_type == "mingtu":
            return Mingtu(Car)


class Car(object):
    def move(self):
        print("car is move!")

    def music(self):
        print("car is music!")

    def stop(self):
        print("car is stop!")


class Suonata(Car):
    pass


class Mingtu(Car):
    pass


car_store = CarStore
car = car_store.order("suonata")
car.move()
car.music()
car.stop()
