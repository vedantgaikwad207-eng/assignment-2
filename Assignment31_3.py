import os 
from datetime import datetime
import schedule
import time 

def Display(x):
    d=0
    e=0
    for a,b,c in os.walk(x):
        for i in b :
            d=d+1
        for i in c :
            e=e+1
    z= datetime.now()
    
    print("Directory Name : ", x)
    print("Number of Files : ", e)
    print("Number of Subdirectories : " , d)
    print("Date and time of scanning : " , z)

def main():
    x=input("Enter the Directory name : ")
    schedule.every(1).minutes.do(Display , x)

    while True :
        schedule.run_pending()
        time.sleep(2)

if __name__=="__main__":
    main()