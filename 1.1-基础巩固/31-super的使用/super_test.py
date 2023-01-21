# -*- coding: UTF-8 -*-
class FooParent(object):
    def __init__(self):
        self.parent = "i am the parent"
        print('Parent')

    def bar(self, message):
        print("%s from parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild, self).__init__()
        print("child")

    def bar(self, message):
        # super(FooChild, self).bar(message)
        print(self.parent)


if __name__ == '__main__':
    child = FooChild()
    # child.bar('hello')
