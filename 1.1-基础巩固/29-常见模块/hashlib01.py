import hashlib
m = hashlib.md5()
print(m)
m.update(b'itcast')
print(m.hexdigest())
