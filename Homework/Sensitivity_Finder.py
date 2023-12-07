list_max=[]
y = 0 
z = 0
minnum = 0.00
maxnum = 0.00
x = 100.00
mean = 0.00
word = ''
while True:
    print(f'{x:.2f}?')  # แสดงผลทศนิยม 2 ตำแหน่ง
    word = input()
    if word == 'D':
        print(f"Your sensitivity is {x:.2f}.")
        break
    elif word == 'F':
        if x <= 100 :
            y+=1
            maxnum = x
            mean = (minnum + maxnum) / 2
            x = mean
        else:
          z=1
          maxnum = x
          mean = (minnum + maxnum) / 2
          x = mean
    elif word == 'S':
        if x <= 100 and y >=1:
            minnum = x
            mean = (minnum + maxnum) / 2
            x = mean
        elif z == 0:
          minnum = x
          maxnum = x*2
          x =maxnum
        elif z==1:
          minnum =x
          mean = (minnum + maxnum) / 2
          x = mean
          