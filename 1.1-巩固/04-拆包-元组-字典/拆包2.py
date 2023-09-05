def test(*args, **kwargs):
    print(args)
    print(*args)  # args表示按照元组格式输出，前面加*表示拆包
    print(kwargs)  # 字典不能拆包


A = (1, 2, 3)
B = (4, 5, 6)
C = {"name": "tom", "age": 18}
print("--1--")
test(A, B, C)

print("--2--")
test(*A, B, C)
print("--3--")
test(*A, *B, C)  # A和B前面加*表示拆包

print("--4--")
# **c只有一作用就是把C放到了第三个print输出得地方
test(*A, *B, **C)
