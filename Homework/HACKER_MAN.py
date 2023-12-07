list_one = ['a', 'f', 'k', 'p', 'u', 'z']
list_two = ['b', 'g', 'l', 'q', 'v']
list_three = ['c', 'h', 'm', 'r', 'w']
list_four = ['d', 'i', 'n', 's', 'x']
list_five = ['e', 'j', 'o', 't', 'y']
hack =25
for i in range(5):
    char = str(input())
    if char in list_one:
        hack -=2
    elif char in list_two:
        hack -=4
    elif char in list_three:
        hack -=6
    elif char in list_four:
        hack-=8
    elif char in list_five:
        hack -=10
if hack <=0:
    print("Unlock")
else:
    print(hack)       
