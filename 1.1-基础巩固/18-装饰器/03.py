def test(func):
    print("kaishiyanzheng")

    def inner():
        print("wokaishiyanzhegnle")
        return func()
    return inner


@test
def test2():
    print("123456")


test2()
