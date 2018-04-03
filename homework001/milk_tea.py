# -*- coding:utf-8 -*-


print("欢迎光临：\n1.原味3元 \n2.香蕉5元\n3.草莓5元\n4.不知道7元\n5.珍珠7元")
kind = int(input("请输入购买品类:\n"))
if 1 <= kind <= 5:

    num = 0
    while num < 1:
        num = int(input("请输入购买数量：\n"))
        if num < 1:
            print("购买数量必须大于一哦")

    card = 2
    while card < 0 or card > 1:
        card = int(input("您是否有会员卡：\n0.没有\n1.有\n"))
        if card < 0 or card > 1:
            print("请不要逗我！！！")

    arr = [0, 3, 5, 5, 7, 7]
    if card == 1:
        sum = arr[kind] * num * 0.9
    else:
        sum = arr[kind] * num
    print("您购买{}号奶茶，共{}杯，请支付{}元".format(kind, num, sum))
else:
    print("sorry，我们只卖特定奶茶")
