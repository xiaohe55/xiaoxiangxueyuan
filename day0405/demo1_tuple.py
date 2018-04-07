'''
元组
元组不支持修改，不支持删除
'''
#定义元组
db_info = ("192.168.1.10",3306,"root","root123")
# ip = db_info[0]
# port = db_info[1]
# print("ip = {}, port = {}".format(ip,port))
# db_info[1] = 3308 #错误，不支持修改
# de db_info[1]  # 错误，不支持删除

# 定义一个元素的元组，最后要有逗号
one_tuple=("zhangsan",)

# 空元祖
none_tuple = ()

#循环遍历元组
for item in db_info:
    print(item)