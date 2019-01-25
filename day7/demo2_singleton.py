# -*- coding:utf-8 -*-
# author:coyote
# datetime:2018/11/28 23:25
# function:单例类
class DataBaseObj(object):
    # 对象初始化
    def __init__(self, new_name):
        print("-----init构造方法----")
        self.name = new_name

    def __new__(cls, name):  # 创建对象
        print("cls_id:", id(cls))
        return object.__new__(cls)  # 必须有返回值，返回的是创建的对象的引用


# print(id(DataBaseObj))
# db = DataBaseObj("mysql")
# print(db)

# 单例类
class SingleInstance:
    __instance = None

    def __init__(self):
        print("---init---")

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


s1 = SingleInstance()
print(id(s1))
s2 = SingleInstance()
print(id(s2))
