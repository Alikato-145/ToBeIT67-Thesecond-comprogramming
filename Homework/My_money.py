'''Hello <i>Judge'''

def main():
    money = int(input())
    money = money/3
    price_kaow = (money/2) - (money*25/200)
    total = money - price_kaow
    print('%.2f' %(total),"Baht")
main()
