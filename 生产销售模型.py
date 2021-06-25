import threading
import time

bread = 0

class Chef(threading.Thread):
    username = ""

    def run(self) -> None:
        global bread

        while True:
            if bread < 500:
                bread += 1
                print(self.username,"做了一个面包!现在还有", bread, "个面包!")
                time.sleep(3)
            else:
                # break
                print("面包篮已经满了,等三秒再做吧!")
                time.sleep(3)

class Customer(threading.Thread):
    username = ""
    money = 1000

    def run(self) -> None:
        global bread
        while True:
            if bread > 0:
                if self.money>= 2:
                    bread -= 1
                    self.money -= 2
                    print(self.username,"买个一个面包!")
                    # time.sleep(2)
                else:
                    break
            else:
                print("没面包了,等两秒吧!")
                time.sleep(2)



chef1 = Chef()
chef2 = Chef()
chef3 = Chef()
cus1 = Customer()
cus2 = Customer()
cus3 = Customer()
cus4 = Customer()
cus5 = Customer()
chef1.username = "张三"
chef2.username = "李四"
chef3.username = "王五"
cus1.username = "小明"
cus2.username = "小红"
cus3.username = "小刚"
cus4.username = "小李"
cus5.username = "小白"

chef1.start()
chef2.start()
chef3.start()
cus1.start()
cus2.start()
cus3.start()
cus4.start()
cus5.start()
