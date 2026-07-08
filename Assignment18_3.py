def main():
    x=int(input("Enter the No. of Elements in the list : "))
    print("Enter the Elements : ")
    Result=[]

    for i in range(x):
        x=int(input())
        Result.append(x)
    x=0
    for i in Result :
        if (i>x):
            x=i
    for i in Result :
        if (i<x):
            x=i
    print("Minimum No. is :", x )

if __name__=="__main__":
    main()