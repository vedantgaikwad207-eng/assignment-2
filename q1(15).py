def main():
    A=list()
    print("Enter No. of elements in lists of No. :")
    x=int(input())
    print("Enter the No. in the lists")
    for no in range(x):
        d=int(input())
        A.append(d)
    print("The square of the No. :")

    square = lambda x : x*x
    
    
    squa=list(map(square,A))
    print(squa)

    


if __name__=="__main__":
    main()