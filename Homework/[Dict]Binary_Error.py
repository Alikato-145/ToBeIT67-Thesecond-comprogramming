dict_num ={}
i=0
while True:
    x=0
    num = str(input())
    if num.upper()== "END":
      break
    else:
      num = int(num)
      if len(dict_num) == 0:
          dict_num.update({num:1})
      else:
          if num in dict_num :
            x = dict_num.get(num)
            x+=1
            dict_num.update({num:x})
          else:
            dict_num.update({num:1})
      i+=1
dict_sorted = sorted(dict_num.items())
dict_sorted = dict(dict_sorted)
for i,j in dict_num.items():
  sum = i+j
  list_sum=[]
  while sum !=0:
    total = sum % 2
    list_sum.append(total)
    sum = sum//2
  list_sum = list_sum[::-1]
  result = 0
  for digit in list_sum:
    result = result * 10 + digit
    dict_sorted.update({i:result})
for i,j in dict_sorted.items():
  print(f'{i}-->{j}')