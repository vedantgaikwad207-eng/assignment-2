def main():
    A=[]
    x=int(input("Enter the No. of elements in the list :"))
    print("Enter the elements :")
    
    for no in range(x):
        z=int(input())
        A.append(z)
    
    odd= lambda x : not(x%2==0)

    squa=list(filter(odd, A))
    print("The odd no. from list are :", squa)



if __name__=="__main__":
    main()