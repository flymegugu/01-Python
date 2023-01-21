import time
t = "2020-10-31 12:44:27"
# 将字符串形式的时间解析为时间元组,手写t为字符串，后面的是字符串展现的格式，然后通过strptime转换为元祖
t = time.strptime(t, "%Y-%m-%d %H:%M:%S")
# <class 'time.struct_time'>
print(type(t))

# 将时间元组格式化为字符串
t = time.strftime("%Y-%m-%d %H:%M:%S", t)  # t前面的我们想看的格式，t为上面通过strptime转换的元祖
# <class 'str'>
print(type(t))
