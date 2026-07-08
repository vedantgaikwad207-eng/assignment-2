import threading
def Thread1(x):
    a=0
    for i in x :
        a=a+i
    print(f"Sum is : {a}")

def Thread2(x):
    a=1
    for i in x :
        a=a*i
    print(f"product is : {a}")
    

def main():
    Result=[]
    x=int(input("Enter the No. of Elements : "))
    print("Enter the Elements : ")
    for i in range(x):
        x=int(input())
        Result.append(x)
    t1 =threading.Thread(target=Thread1 , args =(Result , ))
    t2 =threading.Thread(target=Thread2 , args =(Result , ))
    t1.start()
    t2.start()
    
if __name__=="__main__":
    main()