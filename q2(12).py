def main():
    x=int(input("Enter the no. :"))
    a=1
    
    while(a<=x):
        if(x%a==0):
            print(a," ", end="")
        a=a+1
    
if __name__=="__main__":
    main()
