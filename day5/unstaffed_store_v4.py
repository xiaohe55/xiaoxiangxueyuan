# -*- coding:utf-8 -*-
# author:coyote
# datetime:2018/11/28 23:25
# function:

import datetime
import csv

'''
无人便利店升级版V3
1.增加用户管理系统
2.增加用户购买日志管理系统
3.购物车结算系统升级，增加会员结算
4.增加推荐系统，增加购买量
'''

# -----------------V3 start------------------
# 存储用户信息
g_user_id_set = set()
# 存储用户购买日志
g_bug_logs = []

# -----------------V3 end------------------

# -----------------V4 start------------------
'''
功能：日志管理
'''


class LogManger:

    def get_log_time(self, format):
        """
        获取写日志当前时间
        :param format: 日期格式化方式，如："%Y%m%d"
        :return:
        """
        log_time = datetime.datetime.now().strftime(format)
        return log_time

    def write_log_append_csv(self, file_path, file_name, header, data):
        '''
        将日志追加到CSV文件
        :param file_path: 文件路径
        :param file_name: 文件名称
        :param header: 文件标题
        :param data: 日志数据
        :return:
        '''
        # 写日志时间
        log_time = self.get_log_time("%Y%m%d")
        print("log_time:{}".format(log_time))
        # 文件格式：file_path + file_name + log_time
        # 输出的CSV文件名称
        new_file_name = file_path + file_name + "_" + log_time + ".csv"
        with open(new_file_name, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, header)
            # writer.writeheader()
            writer.writerows(data)


# -----------------V4 end------------------
# 仓库
def wearhouse(item_type):
    # 泡面
    pm_list = ["老坛酸菜", "红烧牛肉", "酸辣粉", "拉面"]
    # 榨菜
    zc_list = ["老干妈", "乌江"]
    # 香肠
    xc_list = ["王中王", "蒜肠", "淀粉肠"]
    if item_type == "pm":
        return pm_list
    elif item_type == "zc":
        return zc_list
    elif item_type == "xc":
        return xc_list


# 检测货架上的商品是否需要补货
def check_add_rack(rack, item_type, item_counts):
    if len(rack) == 0:
        print("正在更新货架，请稍定")
        item_list = wearhouse(item_type)
        while len(rack) < item_counts:
            rack_index = len(rack) % len(item_list)
            rack.append(item_list[rack_index])
        print("商品已上架")


# -----------------V3 start------------------
# 购物车结算系统
def buy_car_account(buy_car, if_vip):
    item_detail = {"老坛酸菜": 5, "红烧牛肉": 4, "酸辣粉": 6, "拉面": 7, "老干妈": 10, "乌江": 2, "王中王": 2, "蒜肠": 12, "淀粉肠": 8}
    total_money = 0
    for item in buy_car:
        total_money += item_detail.get(item, 0)
    if if_vip:
        vip_money = total_money * 0.9
        # 格式化
        total_money = float("%.2f" % vip_money)
    return total_money


# 用户管理系统
# 1.添加新用户 2.判断一个用户是否为VIP
def user_manger_sys(user_id):
    if_vip = False
    if user_id in g_user_id_set:
        if_vip = True
        return if_vip
    else:  # 新用户
        g_user_id_set.add(user_id)
        return if_vip


# 用户购买日志管理系统
# 格式：[{"user_id":"user_id1","money":20,"items":(items1,item2......)}]
def buy_log_manager_sys(user_id, money, *items):
    buy_log = {"user_id": user_id, "money": money, "items": items}
    g_bug_logs.append(buy_log)
    print(buy_log)
    # -----------------V4 start------------------

    item_str = ""
    for item in items:
        if item_str == "":
            item_str = item
        else:
            item_str += '|' + item
    log = LogManger()
    file_path = ""
    file_name = "user_buy_log"
    header = ["user_id", "money", "item"]
    buy_log = [{"user_id": user_id, "money": money, "item": item_str}]
    log.write_log_append_csv(file_path, file_name, header, buy_log)
    # -----------------V4 end------------------


# 推荐系统
def recommend_sys(user_id):
    if user_manger_sys(user_id):  # 通过用户管理系统判断是否为老用户
        user_item_set = set()  # 被推荐人历史购买商品
        other_user_item_dict = {}  # 其他用户历史购买商品{"uset_id":{items,items}}
        for log in g_bug_logs:
            user_id_key = log["user_id"]
            items_value = log["items"]
            if user_id_key == user_id:
                user_item_set.update(items_value)
            else:
                items_set = other_user_item_dict.get(user_id_key)
                if items_set == None:
                    other_user_item_dict[user_id_key] = set(items_value)
                else:
                    items_set.update(items_value)
                    other_user_item_dict[user_id_key] = items_set
        recommend_list = []  # 被推荐列表
        for value_set in other_user_item_dict.values():
            inner_set = user_item_set & value_set
            length = len(inner_set)
            if 0 < length < len(value_set):
                diff_set = value_set - user_item_set
                recommend_list.append({"common_num": length, "items": diff_set})
        if len(recommend_list) > 0:
            recommend_list.sort(key=lambda x: x["common_num"], reverse=True)
            recommend_set = recommend_list[0]["item"]
            return list(recommend_set)  # 集合转化为列表


# -----------------V3 end------------------
# 购物大厅
def shopping_hall():
    # 三个空货架
    pm_rack = []
    zc_rack = []
    xc_rack = []

    # 货架摆放商品数量
    pm_rack_counts = 3
    zc_rack_counts = 3
    xc_rack_counts = 3

    buy_car = []
    if_new_user = True
    while True:
        # 自动检测货架是否需要补货
        check_add_rack(pm_rack, "pm", pm_rack_counts)
        check_add_rack(zc_rack, "zc", zc_rack_counts)
        check_add_rack(xc_rack, "xc", xc_rack_counts)

        if if_new_user:
            print("欢迎光临")
        item_id = int(input("==本店售卖商品：1.泡面 2.榨菜 3.香肠  请输入想要购买的商品编号："))
        if item_id == 1:
            if len(pm_rack) >= 1:
                buy_car.append(pm_rack[len(pm_rack) - 1])
                pm_rack.pop()
            else:
                print("抱歉，泡面已经卖完")
        elif item_id == 2:
            if len(zc_rack) >= 1:
                buy_car.append(zc_rack[len(zc_rack) - 1])
                zc_rack.pop()
            else:
                print("抱歉，榨菜已经卖完")
        elif item_id == 3:
            if len(xc_rack) >= 1:
                buy_car.append(xc_rack[len(xc_rack) - 1])
                xc_rack.pop()
            else:
                print("抱歉，香肠已经卖完")
        else:
            print("请输入在售商品编号！")
            continue

        if_buy = input("请输入y/n选择是否继续购物：")
        if if_buy == "n":
            if len(buy_car) > 0:
                # -----------------V3 start------------------
                if_vip = False
                user_id = ""
                while True:
                    user_id = input("请输入手机号作为用户id使用：")
                    if user_id != "":
                        if_vip = user_manger_sys(user_id)
                        break
                    else:
                        print("输入手机号不能为空，请重新输入")
                total_money = buy_car_account(buy_car, if_vip)
                print("您的购物车商品如下：", buy_car)
                print("您本次消费金额{}元：".format(total_money))
                # 购物日志管理
                buy_log_manager_sys(user_id, total_money, *buy_car)
                recommend_items_list = recommend_sys(user_id)
                if recommend_items_list != None:
                    print("买了该商品的用户还买了{}".format(recommend_items_list))
                # -----------------V3 end------------------
                buy_car = []

                print("欢迎下次光临")
            else:
                print("您没有购买任何商品")
                print("欢迎下次光临")
            break
        else:
            if_new_user = False


shopping_hall()
