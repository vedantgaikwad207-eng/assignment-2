def main():
    print("Enter the No. :")
    x=int(input())
    fact=1
    a=1
    while(a<=x):
        fact=fact*a
        a=a+1
    print(fact)
if __name__=="__main__":
    main()
    