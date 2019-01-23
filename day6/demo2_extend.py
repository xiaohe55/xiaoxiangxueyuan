# -*- coding:utf-8 -*-
# author:coyote
# datetime:2018/11/28 23:25
# function:继承，单继承
class Animal:
    def eat(self):
        print("---吃---")

    def drink(self):
        print("---喝---")

    def run(self):
        print("---跑---")

    def __private_method(self):
        print("私有方法")


class Dog(Animal):
    def hand(self):
        print("---握手---")

class GoldenDog(Dog):
    def guid(self):
        print("我能导航")

wangcai = Dog()
# 调用从父类继承的非私有方法
wangcai.eat()
wangcai.drink()
wangcai.run()

# 父类的私有方法不能被子类继承和调用
# wangcai.__private_method()

# 调用自己的方法
wangcai.hand()

golden = GoldenDog()
golden.eat()
golden.hand()
golden.guid()
