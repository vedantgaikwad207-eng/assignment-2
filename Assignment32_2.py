import os 
import schedule
import datetime
import time 
def Display(x):
    if(not(os.path.exists(x))):
        print("The File doesnt exists ")
        return 
    fobj = open("FileSizeLog.txt" , "a")

    fobj.write(f"File path : {os.path.abspath(x)} \n")
    fobj.write(f"File size : {os.path.getsize(x)} \n")
    fobj.write(f"Date and Time : {datetime.datetime.now()} \n ")

def main():
    x=input("Enter the file name : ")
    schedule.every(30).seconds.do(Display,x)

    while True :
        schedule.run_pending()
        time.sleep(2)

if __name__=="__main__":
    main()
