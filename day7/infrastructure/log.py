# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/1/25 22:07
@file: log.py
@function:
'''
import datetime
import csv


# 日志管理系统
class LogMangerSys:
    def __init__(self):
        self.buy_log = []

    def get_log_time(self, format):
        """
        获取写日志当前时间
        :param format: 日期格式化方式，如："%Y%m%d"
        :return:
        """
        log_time = datetime.datetime.now().strftime(format)
        return log_time

    def write_log_append_csv(self, file_path, file_name, header, data):
        """
        将日志追加到CSV文件
        :param file_path: 文件路径
        :param file_name: 文件名称
        :param header: 文件标题
        :param data: 日志数据
        :return:
        """
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

    def buy_log_manager(self, user_id, money, *items):
        """
        用户购买日志写入到文件
        :param user_id: 用户编号
        :param money: 消费金额
        :param items: 购买商品列表 格式：[{"user_id":"user_id1","money":20,"items":(items1,item2......)}]
        :return:
        """
        buy_log = {"user_id": user_id, "money": money, "items": items}
        self.buy_log.append(buy_log)
        print(buy_log)
        # -----------------V4 start------------------

        item_str = ""  # 格式：老干妈|王中王
        for item in items:
            if item_str == "":
                item_str = item
            else:
                item_str += '|' + item
        file_path = ""
        file_name = "user_buy_log"
        header = ["user_id", "money", "item"]
        buy_log = [{"user_id": user_id, "money": money, "item": item_str}]
        # 调用自身将日志数据写入到CSV文件的方法
        self.write_log_append_csv(file_path, file_name, header, buy_log)
