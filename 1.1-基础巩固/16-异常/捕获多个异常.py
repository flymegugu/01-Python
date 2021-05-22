i = input("输入数值：")
n = 9899
try:
    result = n / int(i)
    print(result)
    print('{0},{1},{2}'.format(n, i, result))
except(ZeroDivisionError, ValueError) as e:
    print("异常内容：{}".format(e))
finally:
    print("释放资源")
