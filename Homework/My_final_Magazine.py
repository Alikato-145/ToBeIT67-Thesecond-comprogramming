bullet = int(input())
heath  = float(input())
damage = float(input())
x = 0 
for i in range(bullet):
    if heath <= 0:
        x=1
        break
    else:
        heath-=damage
        heath = float(heath)
if heath == 0 and bullet == 0 :
    print("dead :",bullet,"bullet remain")
elif x ==1:
    print("dead :",int(bullet-i),"bullet remain")
else: # x=0
    print("alive :",heath,"health")