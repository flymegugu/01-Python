class A(object):
    def __init__(self, a):
        print("the value is %s" % a)


class B(A):
    def __init__(self, b):
        super().__init__("a_value")
        print("hello %s" % b)


B("b")
####
a = 10
b = 20
print("the value ist %s %s" % (a, b))
