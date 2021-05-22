def createNum():
    print("--start--")
    a, b = 0, 1
    for i in range(5):
        print("--A--")
        yield b
        print("--B--")
        a, b = b, a+b
        print("--C--")
    print("--stop--")


a = createNum()


for i in a:  # 此处相当于i接收了生成器a的返回值，这样就可以保证循环次数的上限是由range做设定
    print(i)
