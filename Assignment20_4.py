import threading 

def Small(x):
    count =0
    for i in x :
        if i.islower():
            count = count +1
    print("No. of lowercase is : ", count)

def Capital(x):
    count =0
    for i in x :
        if i.isupper():
            count = count +1
    print("No. of uppercase is : ", count)

def Digits(x):
    count =0
    for i in x :
        if i.isdigit():
            count = count +1
    print("No. of lowercase is : ", count)


def main():
    x=input("Enter the value : ")
    t1=threading.Thread(target = Small , args =(x,))
    t2=threading.Thread(target = Capital , args =(x,))
    t3=threading.Thread(target = Digits , args =(x,))
    print(f"Thread name is : {t1.name}", end ="\n")
    print(f"Thread id is : {t1.ident}")
    
    print(f"Thread name is : {t2.name}")
    print(f"Thread name is : {t2.ident}")
    
    print(f"Thread name is : {t3.name}")
    print(f"Thread name is : {t3.ident}")


    t1.start()
    t2.start()
    t3.start()


if __name__=="__main__":
    main()
    