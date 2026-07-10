import multiprocessing
import os 

def Sumeven(x):
    sum=1
    for i in range(1,x+1):
        
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
    t1=pobj.map(Sumeven , Result)
    print(f"The process ID is : {os.getpid()}")
    pobj.close()
    pobj.join()

    

    print(t1 )  

if __name__=="__main__":
    main()