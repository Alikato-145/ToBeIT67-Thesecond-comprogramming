HP = float(input())
Mana  = float(input())
N  = int(input())
Collect_Mana = 0
X =0
for i in range(N):
    Damage = float(input())
    Collect_Mana +=Damage*0.03
    X +=Damage
if(HP - X <=0):
    print("ดีดี้โดนัท")
elif(HP - Collect_Mana!=0):#ดีดี้ไม่ตาย
  if(Mana > Collect_Mana ):
     print("ตายคู่")
  else:
    print("พาลอยซาชิมิ")