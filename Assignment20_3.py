import threading

result=[]
x=int(input("Enter the No. of ELements :"))
print("Enter the Elements : ")
for i in range(x):
    x=int(input())
    result.append(x)
def Evenlist():
    global result
    c=0

    for i in result:
    
        if(i%2==0):

            c=c+i
    print("sum of evenlist is :", c)

def Oddlist():
    global result 
    
    c=0
    for i in result:
        
        if(not(i%2==0)):
            c=c+i
    print("Sum of oddlist is : ",c)

def main():
    t1=threading.Thread(target = Evenlist)
    t2=threading.Thread(target = Oddlist)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Exit from main")
    

if __name__=="__main__":
    main()