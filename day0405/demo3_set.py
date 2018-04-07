'''
集合
'''

#定义集合
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

#创建空的集合
# none_dict = {} #空字典
# print(none_dict)
# none_set = set()
# print(none_set)


id_list = ["id1","id2","id3","id1","id2"]
distinct_set = set(id_list)
user_id = "id5"
if user_id in distinct_set:
    print(user_id)
if user_id not in distinct_set:
    print("{}不存在".format(user_id))
