import threading 
def fun(no):
    count=1
    for i in range(1,no+1):
        count=count*i
    print(count)

def main():
    x=int(input("Enter the No. :"))
    t1=threading.Thread(target=fun, args=(x,))
    t1.start()

if __name__=="__main__":
    main()