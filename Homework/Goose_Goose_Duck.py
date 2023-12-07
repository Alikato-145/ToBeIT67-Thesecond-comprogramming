import json

name_arr = {}
name_dead = {}
k =0
while True:
    name = input()
    if name == "Start":
        break
    else:
        name_list = json.loads(name)
        name_arr.update(name_list)
while True:
    kill = input()
    if kill == "End":
        break
    else:
        if kill in name_arr:
            name_dead[kill] = name_arr[kill]
            name_arr.pop(kill)
alive = dict(sorted(name_arr.items()))
dead = dict(sorted(name_dead.items()))
for i,l in alive.items():
    if l =="Duck":
        k+=1
print(k,"Ducks Remains")
print("***Alive***")
for i,l in alive.items():
    print(i,":",l)
print("***Dead***")
for i,l in dead.items():
    print(i,":",l)