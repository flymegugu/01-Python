def test(start, stop, step):
    x = start
    while x < stop:  # 当此条件不满足时，也就不会进入到 for循环
        yield x  # yield暂停后返回后面的 x 值，接着才能执行 后面的语句
        x += step


for i in test(1, 4, 1):
    print(i)
