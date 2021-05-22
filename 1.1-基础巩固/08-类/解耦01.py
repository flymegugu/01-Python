class Store(object):
    def order(self, car_type):
        pass


class BMWCarStore(Store):
    def __init__(self):
        self.factory = BMWFactory()


class CarStore(Store):
    def __init__(self):
        self.factory = Factory()
