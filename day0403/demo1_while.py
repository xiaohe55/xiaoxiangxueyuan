'''
while循环
'''

# 打印数字1-10
'''
num = 1
while num <= 10:
    print(num)
    num += 1
'''

# while嵌套 打印沙漏7531357
'''
# 首先打印倒三角
# 1）行号和空格相等
# 2）每行的星号个数=7-行号*2
i = 0  # 行号
while i < 4:
    print(" " * i, end="")  # 打印每行开头的空格
    # print('*'*(7-2*i)) //打印星号
    j = 0  # 控制*的个数
    while j < 7 - i * 2:
        print("*", end="")
        j += 1
    print(" ")
    i += 1
# 打印正三角形状
while i > 0:
    i -= 1
    print(" " * i, end="")  # 打印空格数
    print("*" * (7 - i * 2))
'''

'''
# 合并
m = 7  # 控制行数
i = 0
h = 0  # 空格的个数
middle = m  # 中间位置
while i < m:
    if i < middle:
        h = i
    else:
        h -= 1
    n = m - 4 * 2
    print(" " * h, end="")
    j = 0
    while j < n:
        print("*", end="")
        j += 1
    print("")
    i += 1

'''

'''
# break 跳出循环(只跳出内层)
i = 1
while i<= 20:
    if i % 2 == 0:
        if i % 10 ==0:
            break
        print(i)
    i += 1
 
'''

# continue:结束当次循环
i = 1
while i<= 20:
    i += 1
    if i % 2 == 0:
        if i % 10 ==0:
            continue
        print(i)
