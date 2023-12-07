'''Hello <i>Judge'''

def main():
    name = str(input())
    spec = str(input())
    if(name == "iPhone 15"):
        if(spec =="128 GB"):
            print("32900")
        elif(spec =="256 GB"):
            print("36900")
        else:
            print("Not Sell")
    elif(name == "iPhone 15 Plus"):
        if(spec =="128 GB"):
            print("37900")
        elif(spec =="256 GB"):
            print("41900")
        else:
            print("Not Sell")
    elif(name == "iPhone 15 Pro"):
        if(spec =="128 GB"):
            print("41900")
        elif(spec =="256 GB"):
            print("45900")
        else:
            print("Not Sell")
    elif(name == "iPhone 15 Pro Max"):
        if(spec =="256 GB"):
            print("48900")
        else:
            print("Not Sell")
    else:
        print("Not Sell")
main()
