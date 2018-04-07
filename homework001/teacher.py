"""
    项目名称：小象奶茶馆结算系统
    作者：Jiessie
    时间：2018-3-27
    版本：第一版
"""

print('\n欢迎光临小象奶茶馆！小象奶茶馆售卖宇宙无敌奶茶，奶茶虽好，可不要贪杯哦！每次限尝鲜一种口味：\n 1）原味冰奶茶 3元  2）香蕉冰奶茶 5元 '
      ' 3) 草莓冰奶茶 5元  4）蒟蒻冰奶茶 7元  5）珍珠冰奶茶 7元')
milk_tea_no = input('请选择您要购买的奶茶编号：')

if int(milk_tea_no) <= 5 and int(milk_tea_no) >= 1:

    milk_tea_amount = int(input('请输入您要购买的数量：'))

    if milk_tea_no == "1":
        price = 3
    elif milk_tea_no == "2" or milk_tea_no == "3":
        price = 5
    elif milk_tea_no == "4" or milk_tea_no == "5":
        price = 7

    money = price * milk_tea_amount

    print('您购买的是{}号奶茶，共购买{}杯，总计{}元'.format(milk_tea_no, milk_tea_amount, money))

    if_vip = input('您是小象奶茶馆的会员吗（y/n）？')

    if if_vip == 'y':
        money *= 0.9
        print('您可以享受会员价，折后总价：{}元'.format(money))

else:
    print('Woops!我们只售卖以上五种奶茶哦！新口味敬请期待！')

print("\n********************************************************")
print('\t小象奶茶馆力争做一枚有态度、有思想的奶茶馆（傲娇脸）！\n\t祝您今日购物愉快！诚挚欢迎您再次光临！')
print("********************************************************")

