from functools import reduce 

Ala = lambda x : 70<x<90
Gela = lambda x : x+1
Manogati = lambda x,y : x*y



def main():
    Result=[]
    x=int(input("Enter the No. of elements in list : "))
    print("Enter the No. : ")
    for i in range(x):
        x=int(input())
        Result.append(x)
    Ret1= list(filter(Ala , Result))
    Ret2 = list(map(Gela , Ret1))
    Ret3= reduce(Manogati , Ret2)

    print("list after filter : ", Ret1)
    print("List after map : ", Ret2)
    print("List after reduce : ", Ret3)




if __name__=="__main__":
    main()