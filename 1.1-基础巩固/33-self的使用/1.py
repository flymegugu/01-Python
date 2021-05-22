# coding:utf-8
class Person(object):
    name = None
    age = None

    def run(self):
        print(f'{self.name}在奔跑')

    def jump(self):
        print(f'{self.name}在跳跃')

    def work(self):
        self.run()
        self.jump()
# 这里的函数相当于局部函数

        def sleep(name):
            return name
        result = sleep(self.name)
        print("sleep result is %s" % result)


xiaomu = Person()
xiaomu.name = "tom"
xiaomu.work()
print(dir(Person))
