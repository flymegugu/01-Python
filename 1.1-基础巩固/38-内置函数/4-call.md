call()的本质是将一个类变成一个函数（使这个类的实例可以像函数一样调用）。

class A(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self):
        print('my name is %s' % self.name)
        print('my age is %s' % self.age)

if __name__ == '__main__':
    a = A('jack', 26)
    a()
结果是：

my name is jack
my age is 26

这里定义的类A是需要两个参数的，一个名字一个年龄，我们传入参数后就有了实例a，实例a直接调用就是call方法，这个方法使得a这个类也成为了一个函数，可以调用，也可以为它增加参数，如

def __call__(self， male):
            print('my name is %s' % self.name)
            print('my age is %s' % self.age)
            print('my male is %s' % male)
结果就变为：
my name is jack
my age is 26
my male is man