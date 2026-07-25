from datetime import datetime
import time 
import schedule
import os
def Display():
    timestamp = time.ctime()
    logfname = "Marvellous%s.log"%(timestamp)
    logfname=logfname.replace(" " , "_").replace(":","-")

    fobj = open(logfname , "w")
    fobj.write(f"Log File Created Successfully \n Creation Time : {datetime.now()}")

def main():
    schedule.every(5).seconds.do(Display)
    while True :
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    main()
