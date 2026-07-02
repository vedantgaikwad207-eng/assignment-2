def main():
    
    x=int(input("Enter first no. :"))
    y=int(input("Enter second no. :"))
    
    addition = lambda x,y : x+y
    subtraction = lambda x,y : x-y
    multiplication = lambda x,y : x*y
    division = lambda x,y: x/y

    print("The adddition of two no. is :", addition(x,y))
    print("The subtraction of two no. is :", subtraction(x,y))
    print("The multiplication of two no. is :", multiplication(x,y))
    print("The division of two no. is :", division(x,y))

if __name__=="__main__":
    main()