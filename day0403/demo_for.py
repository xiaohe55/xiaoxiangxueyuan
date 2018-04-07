'''
for循环
'''

'''
# 打印0-9
#range(0,10):[0.1.2.3.4.5.6.7.8.9] 左闭右开
for i in range(10):
    print(i)
'''

'''
# 打印1-9的偶数
for i in range(0, 10, 2):
    print(i)
'''

# break跳出for循环
for i in range(1,5):
    for j in range(0,i):
        if j ==3:
            break
        print("*",end="")
    print("")
    print(i)