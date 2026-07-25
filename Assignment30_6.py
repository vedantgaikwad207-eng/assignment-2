import time
import schedule

def display1():
    print("Lunch Time !")

def display2():
    print("Wrap up work ")

def main():
    schedule.every().day.at("13:00").do(display1)
    schedule.every().day.at("18:00").do(display2)
    while True :
        schedule.run_pending()
        time.sleep(30)
    
if __name__=="__main__":
    main()
