import threading 

def Prime(x):
    count=0
    print("Prime No is : ")

    for i in x:
        for y in range(1,i+1):
            if(i%y==0):
                count=count+1
        if(count==2):
            print(i)
        count=0

def NonPrime(x):
    print("Non Prime No is : ")

    count=0
    for i in x:
        for y in range(1,i+1):
            if(i%y==0):
                count=count+1
        if(not(count==2)):

            print(i)
        count=0
        

def main():
    Result=[]
    x=int(input("Enter the No. of Elements : "))
    print("Enter the Elements : ")
    for i in range(x):
        x=int(input())
        Result.append(x)
    t1 = threading.Thread(target=Prime , args = (Result,))
    t2 = threading.Thread(target = NonPrime , args =( Result,))
    t1.start()
    t1.join()

    t2.start()
    t2.join()
if __name__=="__main__":
    main()
