# -*- coding:utf-8 -*-

'''
input
1. 默认输入类型为String

'''
# card_id =input("请输入卡号：")
# card_passWord =input("请输入密码：")
# print(card_id)
# print(type(card_id))
# print(card_passWord)
#
#
# # print
# print("hello word")
#
# name = "张三"
# print(name)


# card_id =input("请输入卡号：")
# card_passWord =input("请输入密码：")
# print("您的卡号为：",card_id)
# print("您的卡号为：",card_passWord)


#^百分号输出
# card_id = '4856'
# card_passWord=48651
# print("您的卡号为： %s"%card_id)
# print("您的卡号为：%d"%card_passWord)

# 一行输出
# card_id = '4856'
# card_passWord=48651
# print("您的卡号为： %s, 您的卡号为：%d"%(card_id,card_passWord))

# 格式化输出浮点数，并制定精度
# height = 180.55
# print("您的身高为%.2f"%height)

#格式环输出，打印百分号，
# p=99.99
# print("你超越 %.2f%% 用户"%p)

# 无换行输出
# print("hello",end="")
# # print("python")

#输出换行
# print("中国\n北京")

#转义符号
# print("中国\\北京")

#format函数
card_id = '4856'
card_passWord=48651
print("您的卡号为：{}, 您的卡号为：{}".format(card_id, card_passWord))
