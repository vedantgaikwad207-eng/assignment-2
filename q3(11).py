def main():


    x=int(input("Enter the no. :"))

    sum=0
    while(x!=0):
        b=x%10
        sum=sum+b
        x=x//10

    print(sum)

if __name__=="__main__":
    main()
