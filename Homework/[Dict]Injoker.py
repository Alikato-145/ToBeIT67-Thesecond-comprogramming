from itertools import permutations
dict_skill ={"QQQ":"COLD SNAP",
"QQW":"GHOST WALK",
"QQE":"ICE WALL",
"WWW":"E.M.P",
"WWQ":"TORNADO",
"WWE":"ALACRITY",
"EEE":"SUN STRIKE",
"EEQ":"FORGE SPIRIT",
"EEW":"CHAOS METEOR",
"QWE":"DEFEANING BLAST"
}
s = 0#ค่าปุ่มโดนกด
d = 0#ค่าปุ่มโดนกด
S=[]
D=[]
before_SD=[]
x = 0 #ถ้าerror -= 1
name_skill=''
name = str(input())
name = name.upper()
def random_text(X):
  new =X[0]
  result_list=[]
  new_list =[]
  for i in range(len(new)):
    new_list.append(new[i])
  X = list(permutations(new_list))
  for y in X:
     result_list.append("".join(map(str, y)))
  k = 0
  count_repeat = 0
  while k < len(result_list):
      count = result_list.count(result_list[k])
      if count >= 2:
          for j in range(count - 1):
              result_list.remove(result_list[k])
              count_repeat=count
      else:
          k += 1
  return result_list
def check(before_SD,dict_skill,name_skill):
  x  = 0
  for i,j in dict_skill.items():
    for k in before_SD:
      if k ==i:
        name_skill=name_skill+', '+j
      else:
        pass
  return name_skill
list_element = name.split("R")
if "R" not in name:
  print("EZ MID")
else:
  k = 0
  while k < len(list_element):
      count = list_element.count(list_element[k])
      if count >= 2:
          for j in range(count - 1):
              list_element.remove(list_element[k])
      else:
          k += 1
  for i in list_element:
      if "SD" in i :
          s = 1 #กดปุ่ม
          d = 1 
      elif"DS" in i :
          d = 2
          s = 1 
      elif "S" in i:
          s = 1
      elif "D" in i:
          d = 1
      else:
          if len(i) >3: #มากกว่า3
              element = i[-3:]
              x+=2
          elif len(i) ==3:
              element = i
              x+=2
          else: #ต่ำกว่า3,error
              element =''
              x-=1
          before_SD.append(element)
  while len(before_SD)>2:
      before_SD.pop(0)
  if len(before_SD)==2:
    if s == 1 and d ==1:
      D.append(before_SD[0])
      S.append(before_SD[1])
    elif s == 1 and d ==2:
      D.append(before_SD[1])
      S.append(before_SD[0])
    elif s ==1 and before_SD[1]=='':
      S.append(before_SD[0])
    elif d ==1 and before_SD[1]=='':
      x=-100
    elif d ==1 and before_SD[0]=='':
      D.append(before_SD[1])
    elif s == 1 and d ==0:
      S.append(before_SD[1])
    elif s == 0 and d ==1:
      D.append(before_SD[0])
    else:
      x =-1
  else:#len(before_SD) == 1
    if s == 0 and d ==1:
      x =-1
    else:
      S.append(before_SD[0])
  if x  <=0:
    print("EZ MID")
  else:
    if(len(D) == 0 and len(S)>0):
      S = random_text(S)
      name_skill=check(S,dict_skill,name_skill)
      print(name_skill[2:])
    elif(len(D) >0 and len(S)==0):
      D = random_text(D)
      name_skill=check(D,dict_skill,name_skill)
      print(name_skill[2:])
    else:
      S = random_text(S)
      D = random_text(D) 
      for i in S:
        if i == '':
         S.remove(i)
      for i in D:
        if i == '':
         D.remove(i)
      name_skill=check(S,dict_skill,name_skill)
      name_skill=check(D,dict_skill,name_skill)
      print(name_skill[2:])