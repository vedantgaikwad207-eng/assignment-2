import sys 
import os 
import hashlib

def Checksum(Directory):
    fobj = open(Directory , "rb")
    hobj=hashlib.md5()

    Buffer = fobj.read(2000)

    while(len(Buffer)>0):
        hobj.update(Buffer )
        Buffer = fobj.read(2000)
    fobj.close()
    
    
    return hobj.hexdigest()

def main():
    x=sys.argv[1]
    y=sys.argv[2]
    if(len(sys.argv)==3):
        if(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Usage")
            print("The first argument contain .py File name ")
            print("The second and Third argument contain  File name to check the contents  ")
            return 
        
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Help ")
            print("This python file compare the content of files ")
            print("For more info go for --u or --U")
            print("Thank you ")
            return
        else :
            Ret1 = Checksum(x)
            Ret2 = Checksum(y)
            if(Ret1==Ret2):
                print("Success ")
            else :
                print("Failure ")

if __name__=="__main__":
    main()
