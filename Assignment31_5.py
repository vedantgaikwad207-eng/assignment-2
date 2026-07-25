import os 
from datetime import datetime
import schedule
import time 

def Display(x):
    d=0
    e=0
    for a,b,c in os.walk(x):
        
        for i in c :
            e=e+1
    z= datetime.now()
    fobj= open("DirectoryCountLog.txt" , "a")
    fobj.write("Directory Name : ", x)
    fobj.write("Number of Files : ", e)
    
    fobj.write("Date and time of scanning : " , z)

def main():
    x=input("Enter the Directory name : ")
    schedule.every(5).minutes.do(Display , x)

    while True :
        schedule.run_pending()
        time.sleep(2)

if __name__=="__main__":
    main()