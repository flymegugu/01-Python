def makeBold(fn):
    def wrapped():
        print("--1--")
        return "<b>" + fn() + "</b>"
    return wrapped


def makeItalic(fn):

    def wrapped():
        print("--2--")
        return "<i>" + fn() + "</i>"
    return wrapped


@makeBold
@makeItalic  # 先执行最靠近函数的装饰器，转换为test1=makeItalic（test1），返回给test1的值为wrapped，然后又将test1de wrapped传递给makeBlod，
def test1():
    print("--3--")
    return "hello-world"


t = test1()
print(t)
