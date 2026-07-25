import schedule 
import time

def displaymessage(x):
    print(x)

def main():
    x=input("Enter the message : ")
    
    
    schedule.every(5).seconds.do(displaymessage,x)

    
    while True :
        schedule.run_pending()
        time.sleep(1)

    
        
if __name__=="__main__":
    main()
