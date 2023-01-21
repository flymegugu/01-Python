def counter():
    cnt = [0]

    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one


num = counter()
print(num())
