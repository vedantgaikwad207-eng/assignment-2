def main():
    A=[]
    x=int(input("Enter the No. of elements in the lists :"))
    print("Enter the elements :")

    for i in range(x):
        x=int(input())
        A.append(x)
    
    even = lambda x : x%2==0

    squa = list(filter(even , A))
    print(squa)
    

if __name__=="__main__":
    main()