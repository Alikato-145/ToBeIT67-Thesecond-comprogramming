'''Hello <i>Judge'''
def main():
    weight = float(input())
    height = float(input())
    if(weight >0 and height>0):
        BMI = weight / (height/100)**2
        print('%.2f' %(BMI))
    
main()
