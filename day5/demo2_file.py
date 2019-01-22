# -*- coding:utf-8 -*-
# author:coyote
# datetime:2018/11/28 23:25
# function:文件操作

import os
import shutil

# 文件不存在报错
# f = open("test.txt", "r")
# f.close()

# 文件不存在，则创建
'''
f = open('test.txt', 'w', encoding='utf-8') # 覆盖已存在的内容 encoding='utf-8'解决中文乱码
f.write('北京')
f.close()
'''
# 追加内容
'''
f = open('test.txt', 'a', encoding='utf-8')
f.write('\n天津')
f.close()
'''

# read读文件
'''
f = open('test.txt', 'r', encoding='utf-8')
print(f.read())
f.close()
'''
# readlines按行全部读取文件数据，返回一个文件数据列表，每一行是列表中的一个元素
'''
f = open('test.txt', 'r', encoding='utf-8')
data = f.readlines()
print(data)
print("-------------")
i = 1
for line in data:
    print("第{}行：{}".format(i, line), end='')
    i += 1
f.close()
'''
# readline 读一行
'''
f = open('test.txt', 'r', encoding='utf-8')
line1 = f.readline()
print(line1, end='')
line2 = f.readline()
print(line2, end='')
line3 = f.readline()
print(line3, end='')
f.close()
'''

# writelines向文件写入一个字符串序列
'''
f = open('test.txt', 'w', encoding='utf-8')
f.writelines(["张三\n", "李四\n", "王五\n"])
f.close()
'''

# 创建文件夹
# os.mkdir("tes")
# 删除空文件夹
# os.rmdir("tes")
# 删除非空文件夹
# shutil.rmtree("tes")
# 当前目录
# print(os.getcwd())
# 目录列表
# print(os.listdir())

# path = os.getcwd()  # 程序当前路径
# print(path)

# os.chdir("../")  # 切换到上一级目录
# path = os.getcwd()  # 程序当前路径
# print(path)


