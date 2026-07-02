from functools import reduce 

def main():
    A=[]
    x=int(input("Enter the no. of elements in lists : "))
    print("Enter the elements : ")

    for no in range(x):
        x=int(input())
        A.append(x)
    greatest = lambda x,y : x if x>y else y 

    squa=reduce(greatest , A)
    print("The Greatest No is :", squa)

if __name__=="__main__":
    main()