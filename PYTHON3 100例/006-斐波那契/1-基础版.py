# 此方法较占内存 基础版(list方法)
w = int(input("输入一个数字还你一个斐波那契数列："))
list_res = []


def list_n(n):
    if n >= 3:
        res = list_n(n-1)+list_n(n-2)
    else:
        res = 1
    return res


print("开始")

for i in range(0, w):
    list_res.append(list_n(i+1))
print(list_res)
