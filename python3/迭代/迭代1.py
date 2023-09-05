'''
Author: [MaxGu]
Date: 2023-08-05 12:32:12
LastEditors: [MaxGu]
LastEditTime: 2023-09-05 22:41:30
Description:
'''


class Range7:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.current >= self.end:
                raise StopIteration
            if self.num_is_valid(self.current):
                ret = self.current
                self.current += 1
                return ret
            self.current += 1

    def num_is_valid(self, num):
        if num == 0:
            return False
        return num % 7 == 0 or '7' in str(num)
        # a =  num % 7 == 0 or '7' in str(num)
        # print(a)


r = Range7(0, 20)
for num in r:
    print(num)
print(tuple(r))
