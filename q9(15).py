from functools import reduce 

def main():
    A=[]
    x=int(input("Enter the length of list : "))
    print("Enter the Elements : ")
    for i in range(x):
        x=int(input())
        A.append(x)

    mul= lambda x,y : x*y

    squa = reduce(mul , A)
    print("The product of the no. is :", squa)

if __name__=="__main__":
    main()