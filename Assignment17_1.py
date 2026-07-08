from Arithmetic import *

def main():
    x=int(input("Enter the first No. :"))
    y=int(input("Enter the second No. :"))
    print("Addition is : ", Add(x,y))
    print("Subtraction is : ", Sub(x,y))
    print("Multiplication is : ", Mult(x,y))
    print("Division is :", Div(x,y))
    

if __name__=="__main__":
    main()