def main():
    print("Enter the No.")
    x=int(input())
    a=1
    if(not(x%2==0)):
        while(a<=x):
            print(a," ", end="")
            a=a+2
    else:
        x=x-1
        while(a<=x):
            print(a," ",end="")
            a=a+2

if __name__=="__main__":
    main()
    