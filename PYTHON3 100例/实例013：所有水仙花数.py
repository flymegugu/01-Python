for i in range(100, 1000):
    s = str(i)
    one = int(s[0])
    two = int(s[1])
    three = int(s[2])
    if i == one**3+two**3+three**3:
        print(i)