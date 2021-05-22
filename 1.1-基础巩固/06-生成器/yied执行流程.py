def gen():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1


a = gen()
print(next(a))
print(next(a))  # 执行next时，直接来到yield，将yield之后的值返回，然后结束当前next
