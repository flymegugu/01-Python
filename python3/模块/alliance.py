'''
Author: [MaxGu]
Date: 2023-08-03 12:53:25
LastEditors: [MaxGu]
LastEditTime: 2023-08-03 13:42:24
Description:
'''
declaration = "kkkkkkkkk\nkkkkkkkkkkkkk"
print("===========================")
print(declaration)
print("===========================")


def running(distance):
    if distance <= 10000:
        print("ok 我跑", distance, "没问题")
    elif distance > 10000:
        print("我跑不了")
    else:
        print("你在开玩笑？")


def tell_speed(subject):
    hours = int(input("你要几个小时完成？"))
    if hours > 0:
        if hours <= 4:
            print("想要", hours, "完成", subject, "门作业",
                  "你必须", hours/subject*60, "分钟才能完成")
        elif hours <= 6:
            print("超过", hours/subject*60, "就太慢了")
        else:
            print("一门要做", hours/subject*60, "这么久，早点睡吧")
    else:
        print("输入无效")


def dancing():
    import random
    dance = ["<af;lkdjf;aksjfd;;aslkjf;alksjdf;lkasj;fkjasdkfj;lksadjf"]
    print(random.choice(dance))


print(dir())
