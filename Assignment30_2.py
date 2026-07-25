import schedule
from datetime import datetime
import time 
def display():
    print(f"Current Date and Time is {datetime.now()}")

def main():
    schedule.every(1).minutes.do(display)
    while True :
        schedule.run_pending()
        time.sleep(30)

if __name__=="__main__":
    main()