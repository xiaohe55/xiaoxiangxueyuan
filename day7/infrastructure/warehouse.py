# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/1/25 22:07
@file: warehouse.py
@function:
'''

# 仓库管理系统
class WarehouseManageSys:

    def __init__(self):
        # 商品清单
        self.item_detail = {"老坛酸菜": 5, "红烧牛肉": 4, "酸辣粉": 6, "拉面": 7, "老干妈": 10, "乌江": 2, "王中王": 2, "蒜肠": 12, "淀粉肠": 8}

    def get_item_list(self, item_type):
        """
        根据商品类型返回商品列表
        :param item_type: 商品类型
        :return: 商品列表
        """
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

    def add_update_item_info(self, **kwargs):
        """
        添加或更新商品的价格
        :param kwargs: 商品名称好价格的键值对，可以传多个
        :return:
        """
        for item, price in kwargs.items():
            self.item_detail[item] = price
