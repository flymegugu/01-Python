def test1(a, **kwargs):
    print(a)
    print(kwargs)
# **kwargs是将kwargs字典的每一个元素分别拿出来，一次还原成m=100，n=2,但是**kwargs不支持打印出来
#    print(**kwargs)
    test2(**kwargs)


def test2(m, n):
    print(m, n)


test1(1, m=100, n=2)
