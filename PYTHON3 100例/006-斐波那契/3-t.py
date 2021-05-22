target = int(input())
res = 0
a, b = 1, 1
for i in range(target-1):
    a, b = b, a+b
print(a)
