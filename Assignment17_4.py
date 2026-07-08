import threading 
def sum(no):
    count=0
    for i in range(1,no):
        if(no%i==0):
            count=count+i
    print("Sum is : ", count)

def main():
    x=int(input("Enter the No. : "))
    t1=threading.Thread(target=sum,args=(x,))
    t1.start()


if __name__=="__main__":
    main()