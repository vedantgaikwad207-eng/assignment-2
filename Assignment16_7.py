import threading

Div=lambda x :print("True") if x%5==0 else print("False") 
def main():
    x=int(input("Enter the No. : "))

    t1=threading.Thread(target=Div,args=(x,))
    t1.start()

if __name__=="__main__":
    main()
