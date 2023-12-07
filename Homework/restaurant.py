name1 = str(input())
name2 = str(input())
name3 = str(input())
money = 0
def cal(menu,money):
    if menu =="Kai Thot":
        money +=25
    elif menu =="Khao Mu Krop":
        money +=50
    elif menu =="Mu Krathiam":
        money +=45
    elif menu =="Pla Nin Thot":
        money +=80
    elif menu =="Khaoniao":
        money +=5
    return money

money = cal(name1,money)
money = cal(name2,money)
money = cal(name3,money)
print(money,"Baht")