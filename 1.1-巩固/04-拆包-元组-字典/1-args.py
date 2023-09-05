
def test1(a, *args):
    # 输出第一个参数a
    print(a)
    # args是一个元组，里面包括除了第一个参数以外的无名参数
    print(args)
    # *args是将args元组的每一个元素分别拿出来，然后依次打印
    print(*args)


test1(1, 2, 3, 4, 5)
print("--------------")  # 增加分割行
test1(7, (6, 5, 4, 3))
