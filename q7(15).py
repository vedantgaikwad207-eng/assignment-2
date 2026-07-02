def main():
    A=[]
    x=int(input("Enter the length of list"))
    print("Enter the strings in the list :")
    for i in range(x):
        x=input()

        A.append(x)
    
    greater = lambda x : len(x)>5

    squa = list(filter(greater , A))

    print("The strings greater than length 5 is :", squa)
    
    



if __name__=="__main__":
    main()