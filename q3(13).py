def main():
    x=int(input("Enter the no. :"))
    a=1
    b=0
    while(a<x):
        if(x%a==0):
            b=b+a
        a=a+1

    if(x==b):
        print("The given No is perfect no.")
    else:
        print("The given no. is not perfect no.")

if __name__=="__main__":
    main()

