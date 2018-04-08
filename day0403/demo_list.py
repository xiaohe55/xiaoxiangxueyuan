'''
列表
'''
# name_list = ["zhangsan","lisi","wangwu"]
# print(name_list[0])
# print(name_list[1])
# name_list[0] = "xiaobai"
# print(name_list[0])


# 存储不同类型
# info_list = ["zhangsan", 20, 180.5]
# 下标不可越界
# print(info_list[2])
# i = 0
# while遍历
# while i < len(info_list):
#     print(info_list[i])
#     i+=1


# #for 遍历
# for i in range(len(info_list)):
#     print(info_list[i])
# #for 简便
# for item in info_list:
#     print(item)


# 嵌套列表
# infos_list = [["zhangsan", 20, 180.5], ["lisi", 21, 190.5], ["wangwu", 22, 195.5]]
# # print(infos_list[0][0])
# # print(infos_list[1][0])
# for lst in infos_list:
#     print(lst)
#     for item in lst:
#         print(item)

# append 列表末尾添加一个元素
# infos_list = [["zhangsan", 20, 180.5], ["lisi", 21, 190.5], ["wangwu", 22, 195.5]]
# infos_list.append(["xiaobai",30,170])
# print(infos_list)
#

# insert列表指定位置添加元素
# new_info = ["孙悟空", 18, 160]
# new_info.insert(1, 50)
# print(new_info)

# "+"拼接两个列表
# name_list1 = ["zhangsan"]
# name_list2 = ["lisi","wangwu"]
# name_list3 = name_list1 + name_list2
# print(name_list3)


# extend想一个列表中添加列一个列表的元素
# name_list1 = ["zhangsan"]
# name_list2 = ["lisi","wangwu"]
# name_list1.extend(name_list2)
# print(name_list1)

# 删除列表元素
# group = ["tangseng", "wukong", "bajie"]
# 方法一
# del group[1]
# print(group)
# 方法二
# group.remove("bajie")
# print(group)
#方法三
# group.pop()
# print(group)

# in / not in
# group = ["tangseng", "wukong", "bajie"]
# if "tangseng" in group:
#     print("师傅还在，没有被妖怪抓走")
# else:
#     print("师傅没了")



# 排序
# num_list = [5,2,6,1]
# # num_list.sort()#升序
# num_list.sort(reverse=True)#倒序
# print(num_list)

# reverse 将列表内容倒置
# group = ["tangseng", "wukong", "bajie"]
# group.reverse()
# print(group)

#count 指定元素个数
group = ["tangseng", "wukong", "bajie","tangseng"]
count = group.count("tangseng")
print(count)