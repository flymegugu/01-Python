def test():
    i = 0
    while i < 5:
        # 由next出发后看到yield后程序会暂停，然后将yield后面的值(i) 直接返回， 但是  yield i 相当于一个整体 还能接收  send传递过来的值
        temp = yield i  # 第一次next时，执行到这里会先暂停程序，并返回i的值后 再将send传来的 hello1赋值给temp，并且 一次 next 只能激活一次 yield,yied 返回后，表示本次next执行完毕

        print("this is %s" % temp)
        i += 1


t = test()
print(t.__next__())  # 生成器要通过 next或这 __next__() 激活后 才能使用 send
t.send("hello1")  # send从上次yield暂停的位置后开始执行，并在执行前传 hello1 给temp,然后从yield之后执行，当再次碰到yield时候会将yield之后得返回，因为此处没有使用print输出，所以没法通过print对返回后得数值进行打印
print(t.__next__())  # 生成器要通过 next或这 __next__() 激活后 才能使用 send
t.send("hello2")
