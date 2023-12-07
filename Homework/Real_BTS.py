#N24-N8 ฟรีตลอดสาย พอN7เริ่มคิด
#N8-E9,W1-S6 จะเป็นสายเก็บค่าผ่านทางปกติ
#functionเส้นหลักไปถึงสยาม N24-N1-CEN
start = str(input())
end = str(input())
if start == "CEN":
    start_number = 0
elif end == "CEN":
    end_number = 0
count = 0
payment = 0
pay_dict={0:17,
    1:17,
    2:25,
    3:28,
    4:32,
    5:35,
    6:40,
    7:43,
    8:47,
    15:15,
    100:0
}
#23 - 15 = 8
#Ex E23=>E11 => 23-11=12-8=4
#x=0แสดงผลค่ารถปกติ ,x=1แสดงผลError ,x=2แสดงแต่ค่าเหมา x=3 แสดง0
y =0 
x=0
z=0
if start[:1] == end[:1] and start !="CEN":
    start_number = int(start[1:])
    end_number = int(end[1:])
    z=1
    while start_number>end_number:
                y = start_number
                start_number = end_number
                end_number = y
                break
    if start[:1]=='N':
        if end_number ==6 or  start_number == 6:
            x=1
        elif start_number >=8 and end_number >=8:
            x=3
        elif start_number or end_number >8:
            for i in range(start_number,end_number):
                if i >=8:
                    break
                else:
                    count+=1
            if count >6:
                count =6
        else:
            count = abs(start_number-end_number)
            if count>6:
                count =6
    elif start[:1] == 'E':
        if end_number >=14 and  start_number >= 14:
            x=3
        else:
          for i in range(start_number,end_number):
              if i >=15:
                  break
              elif 9<=i<=14:
                  payment = 15
              else:
                  count+=1
          if 9<=start_number <=14 and 9<= end_number <=14:
              x=2
          elif start_number >=15 and end_number >=15:
              x=3
          elif 9<=start_number<=14 and end_number>=14:
            x=2
          else:
              x=0
    elif start[:1] == 'S':
        for i in range(start_number,end_number):
            if 8<=i<=12:
                payment = 15
            else:
                count+=1
        if 8<=start_number <=12 and 8<= end_number <=12:
            x=2
        elif 1<=start_number <=12 and 1<= end_number <=12:
            x=0
        else:
            x=1
    elif start[:1] =='W':
        if start_number and end_number == 1:
            x=0
        else:
            x=1
while z == 0 :
    if start == "CEN" and end == "CEN":
      count = 0
      break
    elif start =="CEN" and end !="CEN":
        start_number = 0
        end_number = int(end[1:])
    elif end =="CEN" and start !="CEN":
        start_number = int(start[1:])
        end_number =0
    else:
        start_number = int(start[1:])
        end_number = int(end[1:])
    while start[:1] =='N' or end [:1] =='N':
        if start[:1] =='N':
            if start_number >8:
                count +=8
            else:
                count +=start_number
        if end[:1] =='N':
            if end_number >8:
                count +=8
            else:
                count +=end_number
        break
    while start[:1] or end [:1] =='E':
        if start[:1] == 'E':
            if start_number >9:
                count +=9
                payment =15
            else: 
                count +=start_number
        if end[:1] =='E':
            if end_number >9:
                count+=9
                payment =15
            else:
                count+=end_number
        break
    while start[:1] or end [:1] =='S':
        if start[:1] == 'S':
            if start_number >8:
                count+=8
                payment = 15
            else:
                count+= start_number
        if end[:1] == 'S':
            if end_number >8:
                count+=8
                payment = 15
            else:
                count+= end_number
        break
    while start[:1] or end [:1] =='W':
        if start[:1] == 'W':
            if start_number>1:
                x=1
            else:
                count+=1
        if end[:1] == 'W':
            if end_number>1:
                x=1
            else:
                count+=1
        break
    break
if count >8:
    count =8
if x == 1:
    print("Error")
elif x ==2:
    print(payment)
elif x ==3:
    print(0)
else:
    print(pay_dict[count]+payment)