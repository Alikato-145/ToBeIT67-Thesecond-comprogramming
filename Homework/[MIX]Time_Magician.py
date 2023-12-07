x = int(input())
y = int(input())
months_31 = [4, 6, 9, 11]
months_30 = [1, 3, 5, 7, 8, 10, 12]
day = 1 #1,1วันพฤหัส
z = 0 
def check_day(day):
  if day == 1:
    print("Thursday")
  elif day ==2:
    print("Friday")
  elif day ==3:
    print("Saturday")
  elif day ==4:
    print("Sunday")
  elif day ==5:
    print("Monday")
  elif day ==6:
    print("Tuesday")
  else:
    print("Wednesday")
for month in range(1, y):
    if month in months_30 :
        day += 30
    elif month in months_31:
        day += 31
    else:
        day += 14
day += x
day = (day-1) % 7
if 0<y <=12 and 0<x <=31:
  if y==2 and x<=14:
    check_day(day)
  elif y in months_30 and x<=30:
    check_day(day)
  elif y in months_31 and x<=31:   
    check_day(day)
  else:
      print("Invalid Time")
else:
  print("Invalid Time")