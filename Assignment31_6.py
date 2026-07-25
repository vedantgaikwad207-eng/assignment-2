import schedule
from datetime import datetime
import time

def display():
    print("Start your weekly Goals ")

def display1():
    print("Review your weekly progress")

def display2():
    print(" Weekly work Completed ")

def main():
    schedule.every().monday.at("9:00")
    schedule.every().wednesday.at("17:00")
    schedule.every().Friday.at("18:00")

    while True :
        schedule.run_pending()
        time.sleep(30)

if __name__=="__main__":
    main()
    