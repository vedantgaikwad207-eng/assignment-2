from functools import reduce 

def ok(No):
    count=0
    for i in range(1,No):
        x=No%i
        count=count+1
    return count==2

ok1 = lambda x : x*2

    
    

def ok2(x):
    a=0
    if(x>a):
        a=x
    return x 

    
    

def main():
    x=int(input("Enter the No. of elements : "))
    print("Enter the elements : ")
    Result =[]
    for i in range(x):
        x=int(input())
        Result.append(x)
    
    Ret1 = list(filter(ok , Result))
    Ret2 = list(map(ok1 , Ret1))
    Ret3 = reduce(ok2 , Ret2)

    print("List after filter : ", Ret1)
    print("List after map :", Ret2)
    print("List after reduce : ", Ret3 )


if __name__=="__main__":
    main()