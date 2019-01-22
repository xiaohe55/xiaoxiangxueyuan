# -*- coding:utf-8 -*-
# author:coyote
# datetime:2018/11/28 23:25
# function:构造方法
class Dog:
    def __init__(self):
        print("我是构造方法，在创建对象时调用")

    def eat(self):
        print("正在吃骨头")

    def drink(self):
        print("正在喝水")


wangcai = Dog()
wangcai.eat()
wangcai.drink()
