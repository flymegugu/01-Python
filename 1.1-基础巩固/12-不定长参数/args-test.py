# 加上星号的形参就要特殊照顾，给你的参数是最多的，你最牛逼，也可以不叫args，可自定义，但必须放到最后位置
def test(a, b, c=22, *args):
    print(a)
    print(b)
    print(c)
    print(args)


#test(1, 2, 3, 4, 5, 6, 7, 8)
# 如果一个元组只有一个元素，那么后面要有一个逗号
#test(1, 2, 3)
# 可以存在空元组
test(1, 2)
