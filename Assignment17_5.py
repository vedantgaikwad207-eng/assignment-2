import threading
def prime(no):
    count=0
    for i in range(1,no+1):
        if(no%i==0):
            count=count+1
    if(count==2):
        print("It is Prime Number ")
    else :
        print("It is not Prime Number ")



def main():
    x=int(input("Enter the No. : "))
    t1=threading.Thread(target=prime, args=(x,))
    t1.start()




if __name__=="__main__":
    main()