import time
import schedule
import os 


def display(x):
    try :
        fobj = open(x , "r")
        Data = fobj.read()

        if(not(os.path.exists(x))):
            print("No Such File found ")

        elif(os.path.getsize==0):
            print("File is empty ")

        else : 
            print(Data)

    except Exception as eobj :
        print("Error occured : " , eobj )

def main():
    x=input("Enter the File Name : ")
    schedule.every(1).minutes.do(display , x)

    while True :
        schedule.run_pending()
        time.sleep(2)

if __name__=="__main__":
    main()

    