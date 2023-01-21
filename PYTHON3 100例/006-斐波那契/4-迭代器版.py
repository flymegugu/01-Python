'''
Author: [MaxGu]
Date: 2022-08-07 18:09:45
LastEditors: [MaxGu]
LastEditTime: 2023-01-19 11:29:18
Description:
'''


class feibo(object):
    def __init__(self, length):
        self.num1 = 0
        self.num2 = 1
        self.num = self.num1
        self.length = length
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num = self.num1
        while True:
            if self.index == self.length:
                raise StopIteration
            self.num1, self.num2 = self.num2, self.num1+self.num2
            self.index += 1
            return self.num


myfbnq = feibo(4)
for i in myfbnq:
    print(i)
#!/bin/bash
#######################################################
# 检测网卡流量，并按规定格式记录在日志中
# 规定一分钟记录一次
# 日志格式如下所示:
# 2019-08-12 20:40
# ens33 input: 1234bps
# ens33 output: 1235bps
# 3
while:

    do
    # 设置语言为英文，保障输出结果是英文，否则会出现bug
    LANG = en
    logfile = /tmp /$(date + %d).log
    # 将下面执行的命令结果输出重定向到logfile日志中
    exec >>$logfile
    date + "%F %H:%M"
    # sar命令统计的流量单位为kb/s，日志格式为bps，因此要*1000*8
    sar - n DEV 1 59 | grep Average | grep ens33 | awk '{print $2,"\t","input:","\t",$5*1000*8,"bps","\n",$2,"\t","output:","\t",$6*1000*8,"bps"}'
    echo "####################"
    # 因为执行sar命令需要59秒，因此不需要sleep
done
