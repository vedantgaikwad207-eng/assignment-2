import schedule
import time
import os 
from datetime import datetime
import sys
import hashlib
from  email.message import EmailMessage
import smtplib

def ChecksumX(x):
    fobj = open(x , "rb")
    Read_Data=fobj.read(1000)

    hobj=hashlib.md5()

    while(len(Read_Data)!=0):
        hobj.update(Read_Data)
        Read_Data=fobj.read(1000)

    return hobj.hexdigest()

def Display(Directory_path , z  ):
    server_email="vedantgaikwad207@gmail.com"
    app_password = "txsy yjdo dvzl mvon"
   
    Total_Files=0
    Deleted_Files=0
    fobj = open("Log_File.txt" , "a")
    
    Duplicate ={}
    checksum_values=[]
    start = time.ctime()
    start_time=time.perf_counter()
    for Folder_name , Sub_Folder, File_Name in os.walk(Directory_path):
        
        for x in File_Name :
            
                    
            Total_Files=Total_Files+1
            x=os.path.join(Folder_name , x)
            checksum=ChecksumX(x)
            if checksum in Duplicate:
                checksum_values.append(checksum)
                Deleted_Files=Deleted_Files+1
                os.remove(x)
            else :
                Duplicate[checksum]=[x]

    end_time=time.perf_counter()
    end=time.ctime()
           
    fobj.write(
        f"\n \n  Starting Time of scanning : {start}"
    )
    
    fobj.write(
        f"\n Completion Time of scanning : {end}"
    )
    fobj.write(f"\n Time required : {end_time-start_time}")
    fobj.write(f"\n Name of Directory scan : {os.path.realpath(Directory_path)}")
    fobj.write(f"\n Total Number of scanned files : {Total_Files}")
    fobj.write(f"\n Total Number of duplicate Files Found : {Deleted_Files}")
    fobj.write(f"\n Total Number of duplicate files deleted : {Deleted_Files}")
    for i in range(len(checksum_values)):
        fobj.write(f"CheckSum values of Duplicate files : {checksum_values[i]} \n ")

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465 )
    server.login(server_email , app_password)
    msg=EmailMessage()
    msg["Subject"]="File details regarding duplicate files"
    msg["from"]=server_email
    msg["To"]=z 

    msg.set_content(
        
        f"""Starting Time of scanning : {start_time} \n
        Completion Time of scanning : {end_time} \n
        Name of Directory scan : {os.path.realpath(Directory_path)} \n
        Total Number of scanned files : {Total_Files} \n
        Total Number of duplicate Files Found : {Deleted_Files} \n
        Total Number of duplicate files deleted : {Deleted_Files} \n """)
    server.send_message(msg)
    server.quit()
        
    
def main():
    try :
    
        if(len(sys.argv)<=1 ):
            print("Invalid arguments")
            print("Please proceed with --h and  --u for Help and usage of the program respectively")
            return
        x=sys.argv[1]
            
        if(len(sys.argv)==4 or len(sys.argv)==3 or len(sys.argv)==2):
            if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
                print("Help")
                print("\n This program is based for scanning the files and deleting the duplicate Files ")
                print("\n For to get the info about usage enter as shown in below : ")
                print("\n python File_Name --u")
                print(" \n Thank You ")
                return 
            elif(sys.argv[1]=="--u" or sys.argv[1]=="--u"):
                print("\n Usage ")
                print("\n For using the program \n Please proceed with the following command line argment ")
                print("\n python File_Name Directory_Path Time_interval Email ")

                return
            elif(not(os.path.isdir(sys.argv[1]))):
                print("The Directory Doesnt exists ")
                return
            
            elif(int(sys.argv[2])<0):
                print("Time Cannot be negative ")
                return
                
                
            elif "@" not in sys.argv[3] :
                print("The third argument is not valid email")
                    
            else :
                y=int(sys.argv[2])
                    
                z=sys.argv[3]

                schedule.every(y).seconds.do(Display , x,z)

                while True :
                    schedule.run_pending()
                    time.sleep(1)
    
    except Exception as eobj :
        print("Error occured : " , eobj )

if __name__=="__main__":
    main()