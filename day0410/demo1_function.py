'''
递归
'''

# for循环实现


# 递归实现
# def recuisive(num):
#     if num > 1:
#         return num * recuisive(num - 1)
#     else:
#         return num
#
# print(recuisive(4))


'''
匿名函数
'''

# sum = lambda x, y: x + y
# #等同于
# # def sum(x, y):
# #     return x + y
#
# print(sum(10, 20))


# 1.匿名函数作为参数传入自定义函数
'''
def x_y_comp(x,y,func):
    rs = func(x,y)
    print(rs)

x_y_comp(3,5,lambda x,y:x+y)
print("--------------------")
x_y_comp(4,6,lambda x,y:x*y)
'''

# 2.匿名函数作为Python内置函数的参数使用
uses_infos = [{"name": "zhangsan", "age": 20}, {"name": "lisi", "age": 17}, {"name": "wangwu", "age": 40}]
print(uses_infos)
# 年龄升序
uses_infos.sort(key=lambda info: info["age"])
print(uses_infos)
# 年龄降序
uses_infos.sort(key=lambda info: info["age"], reverse=True)
print(uses_infos)
