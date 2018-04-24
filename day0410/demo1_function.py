'''
函数
1.局部变量和全局变量
'''

# 局部变量
# def set_name():
#     name = "zhangsan"
#     return name
#
# def get_name(name):
#     # name = "lisi"
#     print(name)
#
# nm = set_name()
# get_name(nm)


# 全局变量
# name = "zhangsan"
# # def get_name():
# #     print(name)
# # def get_name2():
# #     print(name)
# # get_name()
# # get_name2()
# # print(name)


# 修改全局变量的值
# age = 20
# def change_age():
#     # age = 25 #重新定义了一个局部变量age
#     global age
#     age = 25
#     print("函数体内age=%d"%age)
# change_age()
# print("函数体外age=%d"%age)


# 全局变量定义的位置
# g_num3会报错，因为他没有砸函数调用之前
# g_num1 = 100
# def print_global_num():
#     print("g_num1:%d"%g_num1)
#     print("g_num2:%d"%g_num2)
#     print("g_num3:%d"%g_num3)
# g_num2 = 200
# print_global_num()
# g_num3 =300

# 字典、列表作为全局变量，在函数内修改这种类型的全局变量中的元素
# g_num_list = [1,2,3]
# g_info_dict = {"name":"zhangsan","age":20}
# def update_info():
#     g_num_list.append(4)
#     g_info_dict["gender"] = "male"
# update_info()
# print(g_info_dict)
# print(g_num_list)


# 缺省参数:缺省参数在最后
# def x_y_xum(x,y=20):
#     print("X = %d"%x)
#     print("y = %d"%y)
#     return x+y
# rs1 = x_y_xum(10)
# print(rs1)
# rs2 = x_y_xum(10,30)
# print(rs2)

# 错误缺省参数使用方法
'''
def x_y_xum(y=20,x):
    print("X = %d"%x)
    print("y = %d"%y)
    return x+y
'''


# 命名参数
# def x_y_sum (x= 10,y = 20):
#     return x+y
#
# #注意：函数调用时候命名参数的名称与函数定义时的形参名称相同，单数顺序可以不同
# rs1 = x_y_sum(y=30,x=15)
# rs2 = x_y_sum(x=15)
# rs3 = x_y_sum()
#
# print("rs1=%d"%rs1)
# print("rs2=%d"%rs2)
# print("rs3=%d"%rs3)


# 不定长参数
# 第一种def_function([format1_args,]*args)
def any_num_sum(x, y=10, *args):
    print("args={}".format(args))
    rs = x + y
    if len(args) > 0:
        for arg in args:
            rs += arg
    return rs

rs1=any_num_sum(20)
rs2=any_num_sum(20,30)
rs3=any_num_sum(20,30,40,50)

print(rs1)
print(rs2)
print(rs3)

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
# uses_infos = [{"name": "zhangsan", "age": 20}, {"name": "lisi", "age": 17}, {"name": "wangwu", "age": 40}]
# print(uses_infos)
# # 年龄升序
# uses_infos.sort(key=lambda info: info["age"])
# print(uses_infos)
# # 年龄降序
# uses_infos.sort(key=lambda info: info["age"], reverse=True)
# print(uses_infos)
