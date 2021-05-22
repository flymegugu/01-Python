class feibo(object):
    def __init__(self, length):
        self.num1 = 0
        self.num2 = 1
        self.num = self.num1
        self.length = length
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num = self.num1
        while True:
            if self.index == self.length:
                raise StopIteration
            self.num1, self.num2 = self.num2, self.num1+self.num2
            self.index += 1
            return self.num


myfbnq = feibo(4)
for i in myfbnq:
    print(i)
