# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/1/25 22:07
@file: rack.py
@function:
'''

# 货架管理系统
class RackManageSys:

    def check_add_rack(self, rack, item_type, item_counts, wearhouse_manage):
        """
        检测商品是否需要补货
        :param rack: 货架列表
        :param item_type: 商品类型
        :param item_counts: 货架可摆放商品数量
        :param wearhouse_manage: 仓库管理系统对象
        :return:
        """
        if len(rack) == 0:
            print("正在更新货架，请稍定")
            # 根据商品类型从仓库中获取商品列表
            item_list = wearhouse_manage.get_item_list(item_type)
            while len(rack) < item_counts:
                rack_index = len(rack) % len(item_list)
                rack.append(item_list[rack_index])
            print("商品已上架")
