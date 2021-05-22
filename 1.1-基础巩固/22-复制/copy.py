# coding=utf-8
f_name = r'c:\Users\HelloY\Desktop\study\python\hello.py'
with open(f_name,'r',encoding='gbk') as f:
    lines = f.readlines()
    copy_f_name = 'dest_file.txt'
    with open(copy_f_name,'w',encoding='utf-8') as copy_f:
        copy_f.writelines(lines)
        print('文件复制成功')