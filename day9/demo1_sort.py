# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/1/27 13:59
@file: demo1_sort.py
@function:排序算法
'''

# 冒泡
'''
排序的总轮数=列表元素个数 - 1
美伦元素相互比较的次数 = 列表元素个数 - 已经排好序的元素个数-1 
'''


def bubble_sort(data_list):
    '''
    冒泡排序
    :param data_list:待排序列表
    :return:
    '''
    num = len(data_list)  # 列表元素个数
    for i in range(0, num - 1):  # 排序总轮数
        print("第{}轮：".format(i))
        for j in range(0, num - i - 1):
            if data_list[j] > data_list[j + 1]:  # 前后两个元素比较
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
            print(data_list)


# 选择排序
def select_sort(data_list):
    '''
    选择排序
    :param data_list: 待排序列表
    :return:
    '''
    list_len = len(data_list)  # 待排序元素个数
    for i in range(0, list_len - 1):  # 控制排序比较总轮数
        tem_min_index = i
        for j in range(i + 1, list_len):
            if data_list[tem_min_index] > data_list[j]:
                tem_min_index = j
        if i != tem_min_index:
            data_list[i], data_list[tem_min_index] = data_list[tem_min_index], data_list[i]
        print(data_list)


# 快速排序
def quick_sort(data_list, start, end):
    '''
    快速排序
    :param data_list: 待排序列表
    :return:
    '''
    # 设置递归结束条件
    if start >= end:
        return
    low_index = start  # 低位游标
    high_index = end  # 高位游标
    base_data = data_list[low_index]
    while low_index < high_index:
        # 模拟高位游标从右向左指向的元素与基准值进行比较，比基准值大则高位游标一直向左移动
        while low_index < high_index and data_list[high_index] >= base_data:
            high_index -= 1

        if low_index != high_index:
            # 当高位游标指向的元素小于基准值，则移动该值到低位游标指向的位置
            data_list[low_index] = data_list[high_index]
            low_index += 1  # 低位游标向右移动一位

        while low_index < high_index and data_list[low_index] < base_data:
            low_index += 1
        if low_index != high_index:
            data_list[high_index] = data_list[low_index]
            high_index -= 1

    data_list[low_index] = base_data
    # 递归调用
    quick_sort(data_list, start, low_index - 1)  # 对基准值左边未排序队列排序
    quick_sort(data_list, high_index + 1, end)  # 对基准值右边未排序队列排序


# 归并排序
def merge_sort(data_list):
    '''
    归并排序
    :param data_list:待排序列表
    :return:
    '''
    if len(data_list) <= 1:
        return data_list
    # 根据列表长度确定拆分的中间位置
    mid_index = len(data_list) // 2
    # left_list = data_list[:mid_index]  # 使用切片对列表进行拆分
    # right_list = data_list[mid_index:]
    left_list = merge_sort(data_list[:mid_index])
    right_list = merge_sort(data_list[mid_index:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    l_index = 0
    r_index = 0
    merge_list = []
    while l_index < len(left_list) and r_index < len(right_list):
        if left_list[l_index] < right_list[r_index]:
            merge_list.append(left_list[l_index])
            l_index += 1
        else:
            merge_list.append(right_list[r_index])
            r_index += 1
    merge_list += left_list[l_index:]
    merge_list += right_list[r_index:]
    return merge_list


li = [28, 32, 14, 12, 53, 42]
# 冒泡排序
# bubble_sort(li)
# 选择排序
# select_sort(li)
# 快速排序
# quick_sort(li, 0, len(li) - 1)
# 归并排序
new_li = merge_sort(li)
print("-----排序结果-----")
print(new_li)
