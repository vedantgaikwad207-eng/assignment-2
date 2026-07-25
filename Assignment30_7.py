import shutil
import sys
from datetime import datetime
import schedule 
import time 

def display(x,y):
    z=f"{x}_{datetime.now()}.txt"
    shutil.copy(x,z)
    shutil.copy(z,y)
    fobj = open("backup_log.txt", "a")
    fobj.write(f"Backup completed successfully at {datetime.now()}")
    
def main():
    x=sys.argv[1]
    y=sys.argv[2]
    schedule.every(5).seconds.do(display,x,y)
    while True :
        schedule.run_pending()
        time.sleep(20)

if __name__=="__main__":
    main()

    