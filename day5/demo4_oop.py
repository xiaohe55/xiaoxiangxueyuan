# -*- coding:utf-8 -*-
# author:coyote
# datetime:2018/11/28 23:25
# function:面向对象

# 定义类
class Dog:
    def eat(self):
        print("小狗正在啃骨头")

    def drink(self):
        print("小狗正在喝水")


# 创建对象
wang_cai = Dog()
print(id(wang_cai))  # 内存地址
wang_cai.eat()
wang_cai.drink()

a_fu = Dog()
print(id(a_fu))  # 内存地址
a_fu.eat()
a_fu.drink()
