import multiprocessing
import os

def count(x):
    a=0
    count=0
    for i in range(1,x+1):
        for y in range(1,i+1):
            if(i%y==0):
                a=a+1
        if(a==2):
            count=count+1
        a=0
    return count

def main():
    Result=[]
    x=int(input("Enter the No. of ELements : "))
    print("Enter the Elements : ")
    for i in range(x):
        x=int(input())
        Result.append(x)
    
    pobj=multiprocessing.Pool()
    t1=pobj.map(count , Result)
    pobj.close()
    pobj.join()
    
    print(t1 )

if __name__=="__main__":
    main()