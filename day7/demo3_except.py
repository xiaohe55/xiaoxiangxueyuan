# -*- coding:utf-8 -*-
# author:coyote
# datetime:2018/11/28 23:25
# function:异常
'''
try:
    # print(num)
    # print("======")
    open("test.txt", "r")
except NameError as err1:
    print("捕获到异常", err1)
except Exception as err2:
    print("捕获到所有可能异常", err2)

print("哈哈")
'''

# finally的使用

'''
f = None
try:
    f = open("test.txt", 'r')
    print("打印文件内容")
except FileNotFoundError as err:
    print("捕获到了异常", err)
finally:
    print("关闭文件")
    if f != None:
        print("正在关闭文件")
        f.close()
'''

# 函数嵌套：异常传递
'''
def test1():
    print("---test1-1---")
    print(num)
    print("---test1-2---")


def test2():
    try:
        print("---test2-1---")
        test1()
        print("---test2-2---")
    except Exception as err:
        print("捕获到异常！", err)


test2()
'''
