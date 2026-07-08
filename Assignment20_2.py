import threading

def Evenfactor(x):
    c=0

    for i in range(1,x+1):
        if(x%i==0):
            if(i%2==0):

                c=c+i
    print("sum of evenfactor is :", c)

def Oddfactor(x):
    c=0
    for i in range(1,x+1):
        if(x%i==0):
            if(not(i%2==0)):
                c=c+i
    print("Sum of oddfactor is : ",c)

def main():
    x=int(input("Enter the No : "))
    t1=threading.Thread(target = Evenfactor,args=(x,))
    t2=threading.Thread(target = Oddfactor, args=(x,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Exit from main")
    

if __name__=="__main__":
    main()