num = int(input("输入一个数字还你一个斐波那契数列v2.0："))
list_nums = [1, 1]


def calculate(num, list_nums):
    i = 0
    if num > 2:
        while i < num:
            list_nums.insert(i+2, list_nums[i]+list_nums[i+1])
            i += 1
        else:
            print("数列已生成")
            print(list_nums)
        return list_nums[num-1]
    else:
        return list_nums[0]


res = calculate(num, list_nums)
print("="*50)
print("第%s个:%s" % (num, res))
