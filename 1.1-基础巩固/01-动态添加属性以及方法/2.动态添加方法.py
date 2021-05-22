import types


class Person(object):
    def __init__(self, newName):
        self.name = newName


# 实例化一个对象
p1 = Person("tom")

print(p1.name)


# 这样需要使用self来指向绑定的函数
def run(self):
    print("--%s在跑" % self.name)


# 需要通过types.MethodType(run,p1)进行绑定
# p1.run=run()这样是行不通的，因为外部函数run包含了self，所以需要进行绑定，直接p1.run=run（）缺少了self
# 相当于把p1当作参数传给了run方法，p1.run就相当于接受一个返回值，所以p1.run可以任意指定
p1.run = types.MethodType(run, p1)
p1.run()
