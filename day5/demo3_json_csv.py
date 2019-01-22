# -*- coding:utf-8 -*-
# author:coyote
# datetime:2018/11/28 23:25
# function:json和csv文件处理
import json
import csv

json_dict = {"name": "zhangsan", "age": 20, "language": ["python", "java"],
             "study": {"AI": "python", "bigdata": "hadoop"}, "if_vip": True}
'''
# dumps:python to json
json_str = json.dumps(json_dict)
print(json_str)
print(type(json_str))
# loads:json to python
python_data = json.loads(json_str)
print(python_data)
print(type(python_data))
'''

# dump 和load
# with open("user_info.json", "w") as f:  # 文件操作完自动调用close方法关闭
#     json.dump(json_dict, f)
'''
with open("user_info.json", "r") as f:
    user_info_data = json.load(f)
    print(user_info_data)
    print(type(user_info_data))
'''

## csv 文件操作
# 写入CSV文件
'''
datas = [["name", "age"], ["张三", 20], ["李四", 30]]  # 第一个列表表示CSV文件的标题
with open("user_info_csv.csv", 'w', newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    # 一次写入一行
    # for row in datas:
    #     writer.writerow(row)
    # 一次写入多行
    writer.writerows(datas)
'''
# 读CSV文件
'''
with open("user_info_csv.csv", 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)  # reader可迭代对象
    header = next(reader)  # 读一行数据
    print(header)
    print("--------------")
    for row in reader:
        print(row)
        print(row[0])
        print(row[1])
'''

header = ["age", "name"]
rows = [{"name": "zhangsan", "age": 20}, {"name": "lisi", "age": 30}, {"name": "wangwu", "age": 18}]
'''
with open("user_info_csv_dict.csv", 'w', newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f, header)
    writer.writeheader()
    writer.writerows(rows)
'''
with open("user_info_csv_dict.csv", 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
        print("name:{},age:{}".format(row['name'], row['age']))
