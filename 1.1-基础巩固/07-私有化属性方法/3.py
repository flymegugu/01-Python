class A:
    def __init__(self):
        print('a')


class B:
    def __init__(self):
        print('b')


class C1(B, A):
    pass


class C2(A, B):
    pass


class D1(C1):
    def __init__(self):
        C1.__init__(self)


class D2(C2):
    def __init__(self):
        C2.__init__(self)


if(__name__ == '__main__'):
    print('d1------->:')
    d1 = D1()
    print('d2------->:')
    d2 = D2()
