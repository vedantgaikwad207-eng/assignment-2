
def main():

    print("Enter the no. : ")
    x=int(input())
    a=1
    b=0
    while(a<=x):
        if(x%a==0):
            b=b+1
        a=a+1
    
    if(b==2):
        print("The given No is prime no.")
    else:
        print("The given no. is not prime no.")
        

if __name__=="__main__":
    main()