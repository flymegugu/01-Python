#将a，b和args中的数相加
def test(a,b,*args):
    result = a+b 
    for i in args:
        result += i
    print("result=%d"%result)
test(1,2,3,4,5)
