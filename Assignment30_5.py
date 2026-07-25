import schedule
import time 
from datetime import datetime 

def display():
    fobj=open("Marvellous.txt", "a")
    fobj.write(f"Task executed at : {datetime.now()} \n ")

def main():
    schedule.every(5).minutes.do(display)
    while True :
        schedule.run_pending()
        time.sleep(10)

if __name__=="__main__":
    main()
