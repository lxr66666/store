import random

num = random.randint(0,150)

i = 0
gold  = 5000
while i <= 15:

    number = input("请输入您要猜的数：")
    number = int(number)
    if number > num:
        gold -= 500
        i += 1
        print("大了！猜错扣500！")
        print("余额为：",gold)
    elif number < num:
        gold -= 500
        i += 1
        print("小了！猜错扣500！")
        print("余额为：",gold)
    else:
        gold += 3000
        i = 0
        print("恭喜猜中！奖励3000！本次数字为：",num)
        print("余额为：", gold)
        num = random.randint(0, 150)

    if gold == 0 :
        print("余额不足！系统已锁定！")
        break
    if i == 15:
        print("已连续猜错15次！系统已锁定！")
        break