import threading 
ChkNum=lambda x:print("Even no") if  x%2==0 else print("odd no")  


def main():
    x=int(input("Enter the Number "))

    t1=threading.Thread(target=ChkNum , args=(x,))
    t1.start()
    
if __name__=="__main__":
    main()