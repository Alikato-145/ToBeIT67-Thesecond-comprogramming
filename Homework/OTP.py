result =''
while True:
    x = str(input())
    list_count=[0]
    count = 0
    if x == '0':
      break
    if len(x) ==4:
        for i in x:
            if x.count(i) > 1:
                list_count.append(x.count(i))
        if max(list_count) ==2 and list_count.count(max(list_count)) == 2:
          print("Valid")
        else:
          print("Invalid") 
    elif len(x) ==6:
        for i in x:
            if x.count(i) > 1:
                list_count.append(x.count(i))
        if max(list_count) ==2 and list_count.count(max(list_count)) == 4:
          print("Valid")
        elif max(list_count) ==3 and list_count.count(max(list_count)) == 3:
          print("Valid")
        else:
          print("Invalid")
    elif len(x) ==8:
        for i in x:
            if x.count(i) > 1:
                list_count.append(x.count(i))
        if max(list_count) ==2 and list_count.count(max(list_count)) == 6:
          print("Valid")
        elif max(list_count) ==3 and list_count.count(max(list_count)) == 6:
          print("Valid")
        else:
          print("Invalid")