def main():
    x=int(input("Enter the no. :"))
    y=x
    a=0
    while(x!=0):
        b=x%10
        a=a*10+b
        x=x//10


    print("The Reverse no. is :",a)

if __name__=="__main__":
    main()

    
