list_name=[]
while True:
    name = str(input())
    if name.upper() =="END":
        break
    else:
        list_name.append(name)
list_name.sort(key = len)
for i in range(len(list_name)):
    print(list_name[i])