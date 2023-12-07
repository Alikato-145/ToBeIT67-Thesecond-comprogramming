books_before = []  # รายชื่อหนังสือก่อนเรียง
position = []  # ตำแหน่งของหนังสือ
total = []  # จำนวนหนังสือทั้งหมดของแต่ละเล่ม
result = []  # หนังสือหลังจากอยู่บนชั้นแล้ว
x = 0
while True:
    name = str(input())
    x+=1
    y=0
    if name.lower() =='end':
        break
    elif name=="":
        pass
    else:
        if len(books_before) == 0:
            books_before.append(name)
            total.append(len(books_before))
            position.append(x)
        else:
            for i in range(len(books_before)):
                if(books_before[i] == name): #เจอตัวซ้ำ
                    total[i] +=1
                    y = 1
                    break
            if y == 0:
              position.append(x)
              books_before.append(name)
              total.append(1)
for i in range(len(books_before)):
   result.append((books_before[i],position[i],total[i]))
result = sorted(result, key=lambda x:(x[0]))
for x in result:
  print(x[0],x[1],x[2])