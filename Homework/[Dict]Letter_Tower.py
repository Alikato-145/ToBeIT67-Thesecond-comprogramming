char ={}
name = str(input())
for i in range(len(name)):
    if len(char) == 0:
      char.update({name[i]:1})
    else:
      if name[i] in char:
        x = char.get(name[i])
        x+=1
        char.update({name[i]:x})
      else:
        char.update({name[i]:1})
sorted_name = dict(sorted(char.items(), key=lambda item: (-item[1], item[0].lower()))) #เรียงตามตัวอักษร
sorted_f = dict(sorted(sorted_name.items(), key=lambda item:item[1], reverse=True)) #เรียงตามความถี่
print("_________")
for i,j in sorted_f.items():
    print(f'|{i} <-> {j}|')
print("*********")
  