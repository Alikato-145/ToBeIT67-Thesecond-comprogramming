'''Hello <i>Judge'''

def main():
    num1 = str(input())
    num2 = str(input())
    sum1 = num1 + num2
    sum2 = num2 + num1
    sum1 = int(sum1)
    sum2 = int(sum2)
    total = sum1 + sum2
    print(sum1,"+",sum2,"=",total)
main()
