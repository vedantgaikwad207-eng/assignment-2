from  functools import reduce 

Ekdantay = lambda x : x%2==0
vakratunday = lambda x : x*x
gajavakra = lambda x,y : x+y


def main():
    Result=[]

    x=int(input("Enter the No. of elements : "))
    print("Enter the Elements : ")
    for i in range(x):
        x=int(input())
        Result.append(x)

    Ret1=list(filter(Ekdantay , Result ))
    Ret2=list(map(vakratunday,Ret1))
    Ret3=reduce(gajavakra , Ret2)

    print("List after filter : ", Ret1)
    print("List after map : ",Ret2)
    print("list after reduce : ", Ret3)




if __name__=="__main__":
    main()