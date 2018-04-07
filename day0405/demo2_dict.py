'''
字典
'''

# 列表
user_info_list = ["悟空", 100, "男", "取经"]

# 字典,key不能重复
user_info_dict = {"name": "悟空", "age": 100, "gender": "man", "job": "取经"}

# 修改键值内容
# user_info_dict["job"] = "取经|偷桃"
# # print(user_info_dict)

# print("%s的年龄是：%d, 性别：%s, 工作内容： %s"%(user_info_dict["name"],user_info_dict["age"],user_info_dict["gender"],user_info_dict["job"]))


# key不能重复
# user_info_dict = {"name": "悟空", "age": 100, "gender": "man", "job": "取经","job":"偷桃"}
# print(user_info_dict)

# 添加键值对
# user_info_dict["tel"] = "135846248962"
# print(user_info_dict)

# len函数
# print(len(user_info_dict))

# 修改键值对的值
# user_info_dict["age"] = 1000
# print(user_info_dict)

#删除操作,
# del user_info_dict["gender"]
# print(user_info_dict)
# # 删除不存在的键值对写时候，会报错
# del user_info_dict["gender"]


#查询不存在的键---get
#方法一
# if "tel" in user_info_dict:
#     print(user_info_dict["tel"])
# else:
#     print("不存在")

#方法二：其中10010为默认值
# print(user_info_dict.get("tel","10010"))

#遍历--keys获取所有key
# for key in user_info_dict.keys():
#     print("{}:{}".format(key,user_info_dict[key]))
# #values获取所有values
# for value in user_info_dict.values():
#     print(value)

# for item in user_info_dict.items():
#     # print(type(item)) #元组
#     print(item)
#     #元组的键值
#     print(item[0])
#     print(item[1])

# for key,value in user_info_dict.items():
#     print(key)
#     print(value)

#clear清空字典
# user_info_dict.clear()
# print(user_info_dict)
