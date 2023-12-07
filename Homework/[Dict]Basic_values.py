thisdict = {0:"rei",
1:"ichi",
2:"ni",
3:"san",
4:"shi",
5:"go",
6:"roku",
7:"shichi",
8:"hachi",
9:"kyu",
10:"ju",
100:"hyaku"
}
x = int(input())
for i,j in thisdict.items():
    if i ==x:
        print(thisdict[x])
        y=0
        break
    else:
        y=1
if y==1:
    print("Error")
        