
class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge


laowang = Person("老王", 10000)

# 类属性和实例属性可以直接添加 ，如下
laowang.addr = "北京...."
print(laowang.addr)


laozhao = Person("老赵", 18)

# 类属性和实例属性可以直接添加 ，如下
Person.num = 100  # 给类添加属性，然后此类实例化的对象都可以使用
print(laowang.num)
print(laozhao.num)
