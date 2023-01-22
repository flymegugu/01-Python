'''
Author: [MaxGu]
Date: 2022-12-18 22:10:17
LastEditors: [MaxGu]
LastEditTime: 2023-01-22 13:24:18
Description:
'''
s_dict = {102: 'tom', 105: 'amy', 109: 'hi'}
print('----遍历键-----')
for s_id in s_dict.keys():
    print('学号:' + str(s_id))

print('----遍历值----')
for s_name in s_dict.values():
    print('学生:' + s_name)
print('----遍历键：值------')
print(s_dict.items())
for i in s_dict.items():
    print(i)
# for s_id,s_name in s_dict.items():
#    print('学号: {0} - 学生: {1}'.format(s_id,s_name))
