
def test(a):
    count = 0
    for i in range(1, a+1):
        # 通过str转换为字符串，然后从中查看1出现的次数，进行统计
        print(str(i))
        count += str(i).count("1")

    print("一共出现%d次1" % count)


test(41)
