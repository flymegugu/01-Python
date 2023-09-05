info = [
    {"name": "zhangsan", "age": 18},
    {"name": "lisi", "age": 19},
    {"name": "wangwu", "age": 17}
]
# 对该列表按照age进行排序
# 第一种方法


def ke(x):
    return x['age']


info.sort(key=ke)
print(info)
#第二种方法
info.sort(key = lambda x : x["age"])
print(info)