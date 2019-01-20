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
'''
def any_num_sum(x, y=10, *args):
    print("args={}".format(args))
    rs = x + y
    if len(args) > 0:
        for arg in args:
            rs += arg
    return rs


# 改变不定长参数的位置
def any_num_sum2(x, *args, y=10):
    print("args={}".format(args))
    print("x={}".format(x))
    print("y={}".format(y))
    rs = x + y
    if len(args) > 0:
        for arg in args:
            rs += arg
    return rs


rs1 = any_num_sum2(20)
rs2 = any_num_sum2(20, 30, y=100)
rs3 = any_num_sum2(20, 30, 40, 50, 60, 70, 80, y=100)

print(rs1)
print(rs2)
print(rs3)
'''

# 第一种def_function([format1_args,]**args)
# 养老, 医疗，公积金

'''
def social_insurance_comp(basic_money, **proportion):
    print(proportion)
    e_money = basic_money * proportion["e"]
    m_money = basic_money * proportion["m"]
    a_money = basic_money * proportion["a"]
    total_money = e_money + m_money + a_money
    return e_money, m_money, a_money, total_money


e, m, a, t = social_insurance_comp(10000, e=0.2, m=0.1, a=0.12)
print("养老：{},医疗：{},公积金：{},缴费总额：{},".format(e, m, a, t))
'''

# 拆包
# 工资计算器
'''
def salary_comp(basic_money, *other_money, **proportion):
    print("缴费基数：{}".format(basic_money))
    print("其他工资：{}".format(other_money))
    print("比例：{}".format(proportion))


other_money = (500, 200, 100, 1000)
proportion_dict = {'e': 0.2, 'm': 0.1, 'a': 0.12}
# salary_comp(8000, other_money, proportion_dict) #未使用拆包
salary_comp(8000, *other_money, **proportion_dict)
'''

# 递归函数：自身调用自身
'''
1! = 1
2! = 2*1
3! = 3* 2*1
……
n! = n*(n-1)!
'''
# for循环实现
'''
def recursive_for(num):
    rs = num
    for i in range(1, num):
        rs *= i
    return rs


rs = recursive_for(4)
print(rs)
'''

# 递归实现
'''
def recursive(num):
    if num > 1:
        return num * recursive(num - 1)
    else:
        return num


print(recursive(4))
'''

# 匿名函数
'''
sum = lambda x, y: x + y
# 等价函数
# def sum(x, y):
#     return x + y

print(sum(10, 20))
'''

# 1.匿名函数作为参数传入自定义函数
'''
def x_y_comp(x, y, func):
    rs = func(x, y)
    print(rs)


x_y_comp(3, 5, lambda x, y: x + y)
print("--------------------")
x_y_comp(4, 6, lambda x, y: x * y)
'''

# 2.匿名函数作为Python内置函数的参数使用
uses_infos = [{"name": "zhangsan", "age": 20}, {"name": "lisi", "age": 30}, {"name": "wangwu", "age": 18}]
print(uses_infos)
# 年龄升序
uses_infos.sort(key=lambda info: info["age"])
print(uses_infos)
# 年龄降序
uses_infos.sort(key=lambda info: info["age"], reverse=True)
print(uses_infos)
