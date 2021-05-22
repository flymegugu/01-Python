class Dog(object):
    def print_self(self):
        print("dog")


class Xiaotq(Dog):
    def print_self(self):
        print("xiaotq")


def introduce(temp):
    temp.print_self()


dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)
