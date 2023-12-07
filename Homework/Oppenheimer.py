import math
pi = math.pi
r = int(input())
position = int(input())
a = pi*r**2
a = a*2
if(a >=position):
    print("Not Safe")
else:
    print("Safe")