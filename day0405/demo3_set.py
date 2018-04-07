'''
集合
'''

# 定义集合
# student_set = {"zhangsan","lisi","wangwu"}
# print(type(student_set))
# print(len(student_set))
# print(student_set)

# 集合对列表去重，无序存储
# id_list = ["id1","id2","id3","id1","id2"]
# distinct_set = set(id_list)
# print(distinct_set)

# 字符串拆开去重
# string_set = set("hello")
# print(string_set) # {'l', 'o', 'e', 'h'}

# 创建空的集合
# none_dict = {} #空字典
# print(none_dict)
# none_set = set()
# print(none_set)


# id_list = ["id1","id2","id3","id1","id2"]
# distinct_set = set(id_list)
# user_id = "id5"
# if user_id in distinct_set:
#     print(user_id)
# if user_id not in distinct_set:
#     print("{}不存在".format(user_id))

# add 添加元素到集合
# name_set = {"zhangsan","lisi"}
# name_set.add("wangwu")
# print(name_set)

# update(序列):将列表拆分，添加至集合。多个列表仍会去重
# name_set = {"zhangsan","lisi"}
# name_set.update(["悟空","八戒"],["张飞","八戒"])
# print(name_set)

# remove（元素）
# name_set = {"zhangsan","lisi"}
# name_set.remove("zhangsan")
# print(name_set)


# 使用remove删除一个不存在的元素，会报错。要使用dicard
# name_set = {"zhangsan","lisi"}
# name_set.remove("西游记")
# dicard删除一个不存在的元素，不会报错
# name_set.discard("西游记")


# pop()随机删除集合中某个元素，并返回被删除元素
# name_set = {"zhangsan","lisi"}
# print(name_set)
# name = name_set.pop()
# print(name_set)
# print(name)


num_set1 = {1, 2, 3, 4}
num_set2 = {3, 4, 5, 6}
# 交集
# inter_set1 = num_set1 & num_set2
# inter_set2 = num_set1.intersection(num_set2)
# print(inter_set1)
# print(inter_set2)

# 并集
# union_se1 = num_set1 | num_set2
# union_se2 = num_set1.union(num_set2)
# print(union_se1)
# print(union_se2)

# 差集
# diff_set1 = num_set1 - num_set2
# diff_set2 = num_set1.difference(num_set2)
# print(diff_set1)
# print(diff_set2)

#对称差集
sym_diff_set1 = num_set1 ^ num_set2
sym_diff_set2 = num_set1.symmetric_difference(num_set2)
print(sym_diff_set1)
print(sym_diff_set2)