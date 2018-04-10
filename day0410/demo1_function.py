'''
递归
'''


# for循环实现





# 递归实现
def recuisive(num):
    if num > 1:
        return num * recuisive(num - 1)
    else:
        return num

print(recuisive(4))
