class Fib(object):
    def __init__(self, max):
       # super().__init__()
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a+self.b
        return fib


def main():
    fib = Fib(20)
    for i in fib:
        print(i)


# test()
if __name__ == '__main__':
    main()
