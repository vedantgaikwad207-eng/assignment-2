import multiprocessing
import os 

def Sumeven(x):
    sum=0
    for i in range(x+1):
        if(i%2==0):
            sum=sum+1
    return sum

def main():
    Result=[]
    x=int(input("Enter the No. of ELements : "))
    print("Enter the Elements : ")
    for i in range(x):
        x=int(input())
        Result.append(x)
    
    pobj=multiprocessing.Pool()
    t1=pobj.map(Sumeven , Result)
    print(f"The process ID is : {os.getpid()}")
    pobj.close()
    pobj.join()

    

    print(t1 )  

if __name__=="__main__":
    main()