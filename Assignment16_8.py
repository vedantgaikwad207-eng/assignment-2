import threading

def fun(x):
    while(x!=0):
        print("*"," ", end="")
        x=x-1

def main():
    x=int(input("Enter the No. : "))

    t1=threading.Thread(target=fun, args=(x,))
    t1.start()

    

if __name__=="__main__":
    main()