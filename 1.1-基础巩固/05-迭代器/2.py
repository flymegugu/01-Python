def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


print(fib(5))
#print('f5',  fib(5))
#print('f10', fib(10))
