from decimal import Decimal, getcontext

getcontext().prec = 30

num_Itchika = float(input())
num_Nino = float(input())
num_Miku = float(input())
num_Yotsuba = float(input())
num_Itsuki = float(input())
f = float(input())
day = int(input())
pro = 0
y = 5
def score_loop(num, f, day, pro, name, y):
    for i in range(day):
        pro += Decimal(((num / 100) * (f / 100)))
    if pro > 0.6:
        print(name, ": Pass")
    else:
        y -= 1
        print(name, ": Fail")
    return y
y = score_loop(num_Itchika, f, day, pro, "Ichika", y)
y = score_loop(num_Nino, f, day, pro, "Nino", y)
y = score_loop(num_Miku, f, day, pro, "Miku", y)
y = score_loop(num_Yotsuba, f, day, pro, "Yotsuba", y)
y = score_loop(num_Itsuki, f, day, pro, "Itsuki", y)
if y <= 2:
    print("Futaro Outtt!!!")
