def test1(num1):
    print('--1--')

    def test2(num2):
        print('--2--')
        print(num1+num2)
    return test2


t = test1(2)
print("-"*30)
t(3)
