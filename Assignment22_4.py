import multiprocessing
import os
import time

def Cal(x):
    sum=0
    a=1
    for i in range(1,x):
        sum=sum+i**5
    return sum

def main():
    Result=[]
    x=int(input("Enter the No. of ELements : "))
    print("Enter the Elements : ")
    for i in range(x):
        x=int(input())
        Result.append(x)
    start_time=time.perf_counter()
    pobj=multiprocessing.Pool()
    t1=pobj.map(Cal , Result)
    pobj.close()
    pobj.join()

    print(t1 )
    end_time=time.perf_counter()
    print(f"Time required is : {end_time-start_time :.5f}")
    
if __name__=="__main__":
    main()
