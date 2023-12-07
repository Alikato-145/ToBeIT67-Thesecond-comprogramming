x = float(input())
word = "no walking" 
if 8 <= x < 25:
    print("Song Thaeo")
    print("walking")
elif 25 <= x < 40:
    print("Motorcycle")
    print(word) 
elif 40 <= x < 50:  
    print("BTS")
    print("walking")
elif x >= 50:
    print("Taxi")
    print(word)  
else:
    print("stay home")
