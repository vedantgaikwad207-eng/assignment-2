import schedule
import shutil
import time 
import os
import sys

def display(x , y):
    try :
        
        fobj = open("log.txt" , "a")
        
        for a ,b ,c in os.walk(x):
            for d in c :
                d=os.path.join(a,d)
                d=os.path.abspath(d)
                shutil.copy(d , y )
                fobj.write(f"File copied  : {d}")
    except Exception as eobj :
        print("error occured : " , eobj)


def main():
    x=sys.argv[1]
    y=sys.argv[2]
    schedule.every(1).hours.do(display , x , y)

    while True :
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()