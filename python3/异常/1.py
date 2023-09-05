'''
Author: [MaxGu]
Date: 2023-08-09 23:11:36
LastEditors: [MaxGu]
LastEditTime: 2023-08-09 23:13:41
Description:
'''


class xerror(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
