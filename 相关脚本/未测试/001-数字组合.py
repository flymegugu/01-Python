'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-01-23 16:40:56
Description:
'''
total = 0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if ((i != j) and (j != k) and (k != i)):
                print(i, j, k)
                total += 1
print(total)
