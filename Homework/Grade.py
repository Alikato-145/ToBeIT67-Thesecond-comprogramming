'''Hello <i>Judge'''

def main():
    x = float(input())
    if(x>=80):
        print("A")
    elif(75<=x<80):
        print("B+")
    elif(70<=x<75):
        print("B")
    elif(65<=x<70):
        print("C+")
    elif(60<=x<65):
        print("C")
    elif(55<=x<60):
        print("D+")
    elif(50<=x<55):
        print("D")
    else:
        print("F")
main()