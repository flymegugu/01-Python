# python中cls代表的是类的本身
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('self的值为:', self)
# 定义一个build方法，返回一个person实例对象，这个方法等价于Person()。

    @classmethod

    def build(cls):  # 此处的cls相当于Person类
        p = cls("tom", 18)  # 给person类传递值，后实例化一个p对象
        print("cls的值为:", cls)
        return p  # 记得return p 对象



if __name__ == "__main__":
    person = Person.build()  # 因为13行return了 所以可以直接赋值
    print("person的值为:%s" % person, "名字为：%s" %
          person.name, "年龄为:%d" % person.age)

