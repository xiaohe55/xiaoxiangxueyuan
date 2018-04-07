'''
列表
'''
# name_list = ["zhangsan","lisi","wangwu"]
# print(name_list[0])
# print(name_list[1])
# name_list[0] = "xiaobai"
# print(name_list[0])

#info_list = ["zhangsan", 20, 180.5]
#print(info_list[2])
#i = 0
#while遍历
# while i < len(info_list):
#     print(info_list[i])
#     i+=1


# #for 遍历
# for i in range(len(info_list)):
#     print(info_list[i])
# #for 简便
# for item in info_list:
#     print(item)


infos_list = [ ["zhangsan", 20, 180.5], ["lisi", 21, 190.5], ["wangwu", 22, 195.5]]
#print(infos_list[0][0])
#print(infos_list[1][0])
for lst in infos_list:
    print(lst)
    for item in lst:
        print(item)