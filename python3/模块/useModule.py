'''
Author: [MaxGu]
Date: 2023-08-03 13:18:07
LastEditors: [MaxGu]
LastEditTime: 2023-08-05 12:28:21
Description:
'''
import alliance
for i in range(3):
    x = int(input("选个服务吧[1,2,3]:"))
    if x == 1:
        alliance.running(5000)
    elif x == 2:
        alliance.dancing()
    else:
        alliance.tell_speed(5)
