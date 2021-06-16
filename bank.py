import random

# 1.准备数据库和开户行名称
users = {}
'''
    "张三"：{
        "account":"adfadfa",
        "password":"asdfasdf"
    }
'''
bank_name = "中国工商银行昌平支行"


# 银行开户逻辑
def bank_adduser(account, username, password, country, province, street, door):
    # 1.看银行是否已满  满了返回3
    if len(users) > 100:
        return 3

    # 2.用户名是否存在，若存在返回2
    if username in users.keys():
        return 2
    # 3.正常开户，将用户信息存在数据库
    users[username] = {
        "account": account,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": 0,
        "bank_name": bank_name
    }
    return 1


# 用户操作逻辑
def adduser():
    username = input("请输入用户名:")
    password = int(input("请输入取款密码:"))
    country = input("请输入国家:")
    province = input("请输入省份：")
    street = input("请输入街道：")
    door = input("请输入门牌号：")
    account = str(random.randint(10000000, 99999999))  # 8888  --> "8888"
    # 架构数据传输给银行
    status = bank_adduser(account, username, password, country, province, street, door)

    if status == 1:
        print("开户成功！以下是您的个人信息：")
        info = '''
            -------------------个人信息------------------
            用户名:%s,
            密码：%s,
            账号:%s,
            地址：
                国家:%s,
                省份:%s,
                街道：%s,
                门牌号:%s
            余额：%s,
            开户行:%s
        '''
        print(
            info % (username, password, account, country, province, street, door, users[username]["money"], bank_name))

    elif status == 2:
        print("该用户已存在，别瞎弄！")
    elif status == 3:
        print("对不起，数据库已满！请携带证件到其他银行办理！")


def welcome():
    print("--------------------------------------")
    print("-           中国工商银行账户管理系统    -")
    print("--------------------------------------")
    print("-    1.开户                           -")
    print("-    2.存钱                           -")
    print("-    3.取钱                           -")
    print("-    4.转账                           -")
    print("-    5.查询                           -")
    print("-    6.Bye！                          -")
    print("- -------------------------------------")


def bank_save(username, account, save_money):
    if account not in users[username]["account"]:
        return False
    else:
        users[username]["money"] += save_money
        return 1


def save():
    username = input("请输入您的用户名：")
    account = input("请输入您的账户：")
    save_money = int(input("请输入您的存取金额："))

    status = bank_save(username, account, save_money)
    if status == False:
        print("该用户不存在！请重新输入！")
    if status == 1:
        print("存款成功！以下是您的余额信息：")
        info = '''
        -------------------余额信息------------------
        用户名:%s,
        账号:%s,
        余额:%s
        '''
        print(info % (username, account, users[username]["money"]))


def bank_withdraw(username, password, with_money):
    if username not in users.keys():
        return 1
    if password != users[username]["password"]:
        return 2
    if with_money > users[username]["money"]:
        return 3

    users[username]["money"] -= with_money


def withdraw():
    username = input("请输入您的用户名：")
    password = int(input("请输入您的密码："))
    with_money = int(input("请输入您的取款金额："))

    status = bank_withdraw(username, password, with_money)

    if status == 1:
        print("账号不存在！请重新输入！")
    elif status == 2:
        print("密码错误！请重新输入！")
    elif status == 3:
        print("余额不足！穷鬼！")
    else:
        print("取款成功！以下是您的个人信息：")
        info = '''
               -------------------余额信息------------------
               用户名:%s,
               账号：%s,
               余额:%s
               '''
        print(info % (username, users[username]["account"], users[username]["money"]))


def bank_transfer(username, password, username_in, transfer_money):
    if (username or username_in) not in users.keys():
        return 1
    if password != users[username]["password"]:
        return 2
    if transfer_money > users[username]["money"]:
        return 3
    users[username]["money"] -= transfer_money
    users[username_in]["money"] += transfer_money


def transfer():
    username = input("请输入您要转出的账号：")
    password = int(input("请输入您的密码："))
    username_in = input("请输入您要转入的账号：")
    transfer_money = int(input("请输入您要转出的金额："))

    status = bank_transfer(username, password, username_in, transfer_money)
    if status == 1:
        print("您输入的账号有误！请重新输入！")
    elif status == 2:
        print("您输入的密码有误！请重新输入！")
    elif status == 3:
        print("余额不足！穷鬼！")
    else:
        print("转账成功！以下是您的个人信息：")
        info = '''
                       -------------------余额信息------------------
                       用户名:%s,
                       余额:%s
                       '''
        print(info % (username, users[username]["money"]))


def bank_inquire(username, password):
    if username not in users.keys():
        return 1
    if password != users[username]["password"]:
        return 2


def inquire():
    username = input("请输入您的用户名：")
    password = int(input("请输入您的密码："))

    status = bank_inquire(username, password)
    if status == 1:
        print("您输入的账号不存在！请重新输入！")
    elif status == 2:
        print("密码错误，请重新输入！")
    else:
        print("查询成功！以下是您的个人信息：")
        info = '''
                    -------------------个人信息------------------
                    用户名:%s,
                    密码：%s,
                    账号:%s,
                    地址：
                        国家:%s,
                        省份:%s,
                        街道：%s,
                        门牌号:%s
                    余额：%s,
                    开户行:%s
                '''
        print(
            info % (username, password, users[username]["account"],
                    users[username]["country"], users[username]["province"],
                    users[username]["street"], users[username]["door"],
                    users[username]["money"], bank_name))


while True:
    welcome()  # 打印页面
    chose = input("请输入您的业务编号:")
    if chose == '1':
        adduser()
    elif chose == '2':
        save()
    elif chose == '3':
        withdraw()
    elif chose == '4':
        transfer()
    elif chose == '5':
        inquire()
    elif chose == '6':
        print("欢迎再次使用本系统，再见！")
        break
    else:
        print("输入非法，请重新输入！")

