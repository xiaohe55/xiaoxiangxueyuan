# -*- coding:utf-8 -*-
# author:coyote
# datetime:2018/11/28 23:25
# function:继承，单继承
class Animal(object):
    def __init__(self):
        print("A的构造方法")

    def eat(self):
        print("---吃---")

    def drink(self):
        print("---喝---")

    def run(self):
        print("---跑---")

    def __private_method(self):
        print("私有方法")


class Dog(Animal):
    def __init__(self):
        print("Dog的构造方法")

    # 父类方法重写：
    def run(self):
        print("摇着尾巴跑")

    def hand(self):
        # 子类中调用父类的方法：ClassName.methodname(self)
        Animal.run(self)
        print("---握手---")


class GoldenDog(Dog):
    def guid(self):
        print("我能导航")


# wangcai = Dog()
# # 调用从父类继承的非私有方法
# wangcai.eat()
# wangcai.drink()
# wangcai.run()

# 父类的私有方法不能被子类继承和调用
# wangcai.__private_method()

# 调用自己的方法
# wangcai.hand()
#
# golden = GoldenDog()
# golden.eat()
# golden.hand()
# golden.guid()

# 如果在子类中没有定义init的构造方法，则自动调用父类的init的构造方法
# 如果在子类中定义了init构造方法，则不会调用父类的
duoduo = Dog()
# duoduo.hand()
duoduo.run()
