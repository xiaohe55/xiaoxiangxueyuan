'''
字符串内置方法
'''

line = "hello world hello python"

# find
#返回第一次出现时候的角标
#print(line.find("word"))
#指定查找的其实角标
# print(line.find("hello",6))
# 查找不存在的字符，返回-1
#print(line.find("java"))


#count
# print(line.count("hello"))


#replace
#把line中的第一个hello替换为hi
# new_line = line.replace("hello","hi",1)
# print(new_line)

#split，返回列表
# split_list = line.split(" ")
# print(line)
# print(split_list)
#第一个空格
# split_list = line.split(" ",1)
# print(line)
# print(split_list)

#startswith
# print(line.startswith("hello"))
# print(line.endswith("java"))

#应用场景
# files = ["20171201.txt","20171201.log", "20181201.txt", "20181201.log"]
# for file in files:
#     if file.startswith("2018") and file.endswith(".log"):
#         print("2018年待处理日志%s"%file)

#upper和lower
if_continue = input("是否继续购物，输入yes或者no")
if if_continue.lower() =="yes":
    print("继续购物")
else:
    print("再见")