import math
total = 0
pro =0
x = 0
c = 0
while True:
    menu = input()
    if(menu =="stop"):
        break
    elif(menu =="shrimp sour soup"):
        c+=1
        total+=80
    elif(menu =="mixed vegetables sour soup"):
        c +=1
        total+=60
    elif(menu =="papaya sour soup"):
        c +=1
        total+=55
    elif(menu =="snapper fish sour soup"):
        c +=1
        total+=100
    elif(menu =="cha om shrimp sour soup"):
        c +=1
        total+=100
if(total>200 and c>=3):
    pro = total*0.15
    x = total - pro
    pro = math.floor(pro)
    x = math.floor(x)
    print("Original Price",total,"baht")
    print("Discount",pro,"baht")
    print("Total",x,"baht")
else:
    print("Original Price",total,"baht")
    print("Discount 0 baht")
    print("Total",total,"baht")