'''
Author: [MaxGu]
Date: 2023-08-06 22:29:34
LastEditors: [MaxGu]
LastEditTime: 2023-08-07 13:12:50
Description:
'''
x = input("0-4")
if x not in ['0', '1', '2', '3', '4', '5']:
    print("无异常")
    import sys
    sys.exit(0)
else:
    try:
        triger = int(x)
        if triger == 0:
            e = 1/0
        if triger == 1:
            a = [1, 2, 3, 4, 5, 16]
            print(a[6])
        if triger == 2:
            a = '2'+3
        if triger == 3:
            import notExxxx
        if triger == 4:
            b
            print("b=", b)
        if triger == 5:
            print("无异常分支")
    except IndexError:
        print("越界")
    except ZeroDivisionError:
        print("除0了")
    except (ModuleNotFoundError, NameError):
        print("不存在或名字错了")
    except:
        print("有其他异常")
