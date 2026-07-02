def main():
    a=0
    print("Enter the no. :")
    x=int(input())
    
    
    while(x!=0):
        
        a=a+1
        x=x//10

    print("The no. of digits is :", a)



if __name__=="__main__":
    main()