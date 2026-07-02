def main():
    A=[]
    x=int(input("Enter the length of the list : "))
    print("Enter the Elements : ")
    for i in range(x):
        x=int(input())
        A.append(x)
    
    even = lambda x : x%2==0

    squa= len(list(filter(even, A)))

    print("The length of filtered list is : ", squa)

if __name__=="__main__":
    main()
