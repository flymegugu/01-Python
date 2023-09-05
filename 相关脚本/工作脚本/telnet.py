'''
Author: [MaxGu]
Date: 2023-05-11 16:40:21
LastEditors: [MaxGu]
LastEditTime: 2023-08-09 09:16:34
Description:
'''
# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# 批量测试端口号
import pandas as pd
import os
import telnetlib
import socket
# 读取Excel
df = pd.read_excel(
    r'D:\domain.xlsx')
domain_item = df.columns[0]  # 域名列
port_item = df.columns[1]  # 端口列
result = []
for i in df.index:
    domain = df.loc[i][domain_item]  # 读取域名
    port = int(df.loc[i][port_item])
    # 读取端口
    tc = telnetlib.Telnet()
    try:
        tc.open(domain, port, 1)  # 检测telnet端口
    except Exception as e:
        status = "不通"
        try:
            IP = socket.getaddrinfo(domain, port)[0][-1][0]  # 获取域名解析
            print(IP)
        except Exception as e:
            print(e)
            IP = 'unknown'
    else:
        status = "通"
        IP = tc.get_socket().getpeername()[0]  # 获取域名解析
        tc.close()
    # line = [num, domain, port, status, IP]  # 本行的数据
    line = [domain, port, status, IP]  # 本行的数据
    result.append(line)  # 纳入本行数据到result
# 生成DataFrame 导出结果excel
#df = pd.DataFrame(result, columns=['域名', '端口', '通否', 'IP'])
df = pd.DataFrame(result, columns=['域名', '端口', '通否', 'IP'])
df.to_excel('D:\domain1.xlsx', index=False)
