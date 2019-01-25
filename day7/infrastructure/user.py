# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/1/25 22:10
@file: user.py
@function:
'''

# 用户管理系统
class UserManageSys:
    def __init__(self):
        self.user_id_set = set()

    def add_new_user(self, user_id):
        """
        添加新用户
        :param user_id:用户编号
        :return:
        """
        if user_id in self.user_id_set:
            self.user_id_set.add(user_id)

    def if_vip(self, use_id):
        """
        验证用户是否为VIP
        :param use_id: 用户编号
        :return:
        """
        if use_id in self.user_id_set:
            return True
        else:
            return False


# 购物车
class BuyCar:
    def __init__(self, user_id, user_manage):
        self.user_id = user_id
        # 验证是否为VIP
        self.if_vip = user_manage.if_vip(self.user_id)
        # 初始化一个购物车车筐
        self.buy_car = []

    def add_item_2_car(self, pm_rack, zc_rack, xc_rack, item_id):
        """
        向购物车添加商品
        :param item_id: 商品编号
        :param pm_rack: 泡面货架
        :param zc_rack: 榨菜货架
        :param xc_rack: 香肠货架
        :return:
        """
        if item_id == 1:
            if len(pm_rack) >= 1:
                self.buy_car.append(pm_rack[len(pm_rack) - 1])
                pm_rack.pop()
            else:
                print("抱歉，泡面已经卖完")
        elif item_id == 2:
            if len(zc_rack) >= 1:
                self.buy_car.append(zc_rack[len(zc_rack) - 1])
                zc_rack.pop()
            else:
                print("抱歉，榨菜已经卖完")
        elif item_id == 3:
            if len(xc_rack) >= 1:
                self.buy_car.append(xc_rack[len(xc_rack) - 1])
                xc_rack.pop()
            else:
                print("抱歉，香肠已经卖完")
        else:
            print("请输入在售商品编号！")

    def account(self, warehouse_manage):
        """
        购物车结算
        :param warehouse_manage:仓库管理系统对象，用于获取商品价格清单
        :return:
        """
        total_money = 0
        for item in self.buy_car:
            total_money += warehouse_manage.item_detail.get(item, 0)
        if self.if_vip:
            vip_money = total_money * 0.9
            # 格式化
            total_money = float("%.2f" % vip_money)
        return total_money

