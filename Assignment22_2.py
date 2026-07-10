import multiprocessing
import os 

def Fact(x):
    sum=1
    for i in range(1,x):
        sum=sum*i
    return sum

def main():
    Result=[]
    x=int(input("Enter the No. of ELements : "))
    print("Enter the Elements : ")
    for i in range(x):
        x=int(input())
        Result.append(x)
    
    pobj=multiprocessing.Pool()
    print(f"Process id is : {os.getpid()}")
    t1=pobj.map(Fact , Result)
    pobj.close()
    pobj.join()
    print(t1)
    

if __name__=="__main__":
    main()