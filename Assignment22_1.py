import os 
import multiprocessing

def Square(x):
    sum=0
    
    for y in range(x):
        sum=sum+y*y
        
        
    return sum 


def main():
    Result=[]
    x=int(input("Enter the No. of ELements : "))
    print("Enter the Elements : ")
    for i in range(x):
        x=int(input())
        Result.append(x)
    
    pobj=multiprocessing.Pool()
    t1=pobj.map(Square , Result)
    print(t1 )

if __name__=="__main__":
    main()