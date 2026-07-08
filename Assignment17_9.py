def main():
    x=int(input("Enter the No. : "))
    a=0
    sum=0
    while(x!=0):
        a=x%10
        sum=sum+1
        x=x//10
    print("The No. of digits is :", sum)
        


if __name__=="__main__":
    main()