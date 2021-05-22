# coding = utf-8
# 4s店例子
class CarStore(object):
    def order(self, car_type):
        if car_type == "suonata":
            return Suonata()
        elif car_type == "mingtu":
            return Mingtu()


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
