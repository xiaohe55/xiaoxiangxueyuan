'''
函数
'''

# 函数定义
# def print_user_info():
#     print("name:zhangsan")
#     print("age:20")
#     print("gender:man")
# print_user_info()

# 带参函数注意：
# 1.调用函数时传入的参数个数与函数定义参数个数相同
# 2、 参数顺序要相同
# def print_user_info2(name,age,gender):
#     print("name: %s"%name)
#     print("age: %d"%age)
#     print("gender: %s"%gender)
# print_user_info2("悟空",1000,"man")
# print_user_info2("八戒",990,"man")


# 有返回值函数
# def x_y_sum_return(x, y):
#     res = x + y
#     return res
# z = x_y_sum_return(2, 3)
# print(z)

# 返回list
'''

def x_y_sum_com_list(x, y):
    res1 = x + y
    res2 = x * y
    res_list = [res1, res2]
    return res_list
print(x_y_sum_com_list(2, 3))
'''


# 返回元组
# 方法一：
# def x_y_sum_com_tuple(x, y):
#     res1 = x + y
#     res2 = x * y
#     res_tuple = (res1, res2)
#     return res_tuple
# print(x_y_sum_com_tuple(2, 3))
# 方法二
def x_y_sum_com_tuple2(x, y):
    res1 = x + y
    res2 = x * y
    return res1, res2


print(x_y_sum_com_tuple2(2, 3))
a, b = x_y_sum_com_tuple2(2, 9)
print(a)
print(b)
