from functools import reduce

add= lambda x,y : x+y


def main():
    x=int(input("Enter the No. of Elements in the list : "))
    print("Enter the Elements : ")
    Result=[]
    sum=0
    for i in range(x):
        x=int(input())
        Result.append(x)

    squa = reduce(add,Result)        
    
    print("Sum is : ", squa)
if __name__=="__main__":
    main()
