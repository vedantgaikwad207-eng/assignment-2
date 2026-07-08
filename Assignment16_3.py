import threading 

Add=lambda x,y:print("Addition is : ", x+y)



def main():
    x=int(input("Enter the first no. :"))
    y=int(input("Enter the second no :"))

    t1=threading.Thread(target=Add, args=(x,y,))
    t1.start()




if __name__=="__main__":
    main()