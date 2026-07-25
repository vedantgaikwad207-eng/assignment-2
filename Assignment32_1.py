import schedule 
import time
from datetime import date  , datetime

def display():
    now = datetime.now()
    timestamp = time.ctime()


    logfname="File %s.txt"%(timestamp)
    logfname = logfname.replace(" " , "_").replace(":","_")


    fobj = open(logfname , "w")
    fobj.write(f"Filename : {logfname}")
    fobj.write(f"Creation Date : {date.today()}")
    fobj.write(f"Creation Time : {now.hour}:{now.minute}:{now.second} ")

               

def main():
    schedule.every(1).minutes.do(display)

    while True :
        schedule.run_pending()
        

if __name__=="__main__":
    main()


