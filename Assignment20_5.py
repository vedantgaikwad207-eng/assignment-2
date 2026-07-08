import threading 



def t1():
    for i in range(1,51,1):
        print(i , " ", end ="")

def t2():
    for i in range(50,0,-1):
        print(i , " ", end ="")

def main():
    Thread1=threading.Thread(target = t1)
    Thread1.start()
    print(end="\n")
    Thread2=threading.Thread( target = t2)
    Thread2.start()

if __name__=="__main__":
    main()