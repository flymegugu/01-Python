class Dog:
    def __init__(self,name,age,sex="女孩"):
        self.name = name
        self.age = age
        self.sex = sex 
    def run(self):
        print("{0}is  running".format(self.name))
    def speak(self,sound):
        print("{0} is speak {1}".format(self.name,sound))

dog = Dog('球球',2)
dog.run()
dog.speak('旺旺旺')