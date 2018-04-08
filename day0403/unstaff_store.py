'''
无人便利店
'''

# 三个空货架
pm_rack = []
zc_rack = []
xc_rack = []

# 向货架摆货
# 泡面
pm_list = ["老坛酸菜", "红烧牛肉", "酸辣粉", "拉面"]
pm_rack_num = 3
while len(pm_rack) < pm_rack_num:
    pm_index = len(pm_rack) % len(pm_list)
    pm_rack.append(pm_list[pm_index])
# 榨菜
zc_list = ["老干妈", "乌江"]
zc_rack_num = 3
while len(zc_rack) < zc_rack_num:
    zc_index = len(zc_rack) % len(zc_list)
    zc_rack.append(zc_list[zc_index])
# 香肠
xc_list = ["王中王", "蒜肠", "淀粉肠"]
xc_rack_num = 3
while len(xc_rack) < xc_rack_num:
    xc_index = len(xc_rack) % len(xc_list)
    xc_rack.append(xc_list[xc_index])

buy_car = []
while True:
    if len(pm_rack) == 0 and len(zc_rack) == 0 and len(xc_rack) == 0:
        print("所有商品已经售罄")
        break
    goods_num = int(input("==本店售卖商品：1.泡面 2.榨菜 3.香肠  请输入想要购买的商品编号："))
    if goods_num == 1:
        if len(pm_rack) >= 1:
            buy_car.append(pm_rack[len(pm_rack) - 1])
            pm_rack.pop()
        else:
            print("抱歉，泡面已经卖完")
    elif goods_num == 2:
        if len(zc_rack) >= 1:
            buy_car.append(zc_rack[len(zc_rack) - 1])
            zc_rack.pop()
        else:
            print("抱歉，榨菜已经卖完")
    elif goods_num == 3:
        if len(xc_rack) >= 1:
            buy_car.append(xc_rack[len(xc_rack) - 1])
            xc_rack.pop()
        else:
            print("抱歉，香肠已经卖完")
    else:
        print("请输入在售商品编号！")
        continue

    if len(buy_car)> 0:
        print("你的购物车商品如下:",buy_car)
    else:
        print("没有购买任何商品")

    if_buy = input("请输入y/n选择是否继续购物：")
    if if_buy == "n":
        break

print("欢迎下次光临")
