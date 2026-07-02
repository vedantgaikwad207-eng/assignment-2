from functools import reduce 

def main():
    A=[]
    x=int(input("Enter the No. of the elements in the list"))
    print("Enter the elements :")
    for no in range(x):
        x=int(input())
        A.append(x)
    add=lambda x,y: x+y

    squa=reduce(add,A)
    print("The Addition is :", squa)

if __name__=="__main__":
    main()