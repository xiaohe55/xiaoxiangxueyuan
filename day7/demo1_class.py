# -*- coding:utf-8 -*-
# author:coyote
# datetime:2018/11/28 23:25
# function:类属性
class Person:
    # 类属性
    sum_num = 0

    def __init__(self, new_name):
        # 实例属性
        self.name = new_name
        # 定义一个与类属性同名的实例属性
        # self.sum_num = new_num
        # 修改类属性值，每创建一个实力对象，类属性值加一
        # Person.sum_num += 1

    # 类方法
    @classmethod
    def add_sum_num(cls):
        cls.sum_num += 1
        print(cls.sum_num)

    # 静态方法
    @staticmethod
    def static_test():
        print("----静态方法------")
        Person.sum_num += 1
        print(Person.sum_num)


'''
p1 = Person("zhagnsan")
# print(p1.sum_num, Person.sum_num)
# 通过实力对象不能够修改类属性值，如果修改的属性在事例中不存在，则动态添加实例属性
p1.sum_num = 100
p2 = Person("lisi")
print(p1.sum_num, p2.sum_num, Person.sum_num)
'''

# 类属性与实例属性同名调用举例
'''
p1 = Person("zhangsan", 10)
print(p1.sum_num, Person.sum_num)
'''

# 类方法调用
'''

# 方法一：类名.类方法
Person.add_sum_num()
print("-----------------")
# 方法二：实力对象.类方法(不推荐)
p = Person("zhangsan")
p.add_sum_num()
'''

# 静态方法调用
Person.static_test()
print("-----------------")
p = Person("zhangsan")
p.static_test()

# 总结：在类方法和静态方法中不能直接调用实例属性