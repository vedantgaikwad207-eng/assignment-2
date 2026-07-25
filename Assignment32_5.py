import schedule
import time
import os
import sys

def Display(x):
    try :
        fobj = open("log1.txt" , "a")
        for a ,b,c in os.walk(x):
            for d in c :
                d=os.path.join(a,d)
                if(os.path.getsize(d)==0):
                    fobj.write(f"{os.path.abspath(d)}")
                    os.remove(d)
            print("Files removed successfully ")
    except Exception as eobj :
        print("Error occured : " , eobj)
    

def main():
    x=sys.argv[1]
    schedule.every(1).hours.do(Display,x)

    while True :
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
