def test(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

    #{'d': 100, 'e': 200}
    # 要分配给kwargs的话，必须保证传入的参数有=号赋值
test(1, 2, 3, 4, 5, d=100, e=200)
