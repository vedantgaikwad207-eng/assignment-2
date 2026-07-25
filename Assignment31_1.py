import schedule 
import time

def display(x):
    print(x)

def main():
    x=input("Enter the message : ")
    y=int(input("Enter the Interval in seconds : "))
    if(x>0):
        schedule.every(y).seconds.do(display,x)

    
    while True :
        schedule.run_pending()
        time.sleep(1)

    else:
        print("Time cant be negative ")
        
if __name__=="__main__":
    main()
