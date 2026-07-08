import threading

def display():
    x=int(input("Enter the No. : "))
    if(x<0):
        print("Negative No.")
    elif(x>0):
        print("Positive No. ")
    else :
        print("Zero")

def main():
    t1=threading.Thread(target=display)
    t1.start()
    


if __name__=="__main__":
    main()