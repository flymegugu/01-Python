class Person(object):
    def __hello(self, data):
        print("hello %s" % data)
# 通过类中的公有方法对类中的私有方法进行调用，这也是封装的意义所在

    def helloworld(self):
        self.__hello("world")


t = Person()
t.helloworld()
