def main():
    x=int(input("Enter the No. of the Elements : "))
    Result =[]
    for i in range(x):
        x=int(input())
        Result.append(x)
    y=int(input("Enter the No. to search : "))
    count=0
    for i in Result :
        if(i==y):
            count=count+1
    
    print("No. of frequency of that No. occured : ", count)



if __name__=="__main__":
    main()