def main():
    x=int(input("Enter the no. :"))
    c=0
    y=x
    while(x!=0):
        b=x%10
        c=c*10+b
        x=x//10
    if(y==c):
        print("The given no. is palindrome ")

    else:
        print("The given no. is not palindrome ")

if __name__=="__main__":
    main()