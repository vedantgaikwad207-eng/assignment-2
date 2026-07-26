import psutil
import os
import sys
import schedule
import time 

def display(x):

    listprocess=[]
    for process in psutil.process_iter():
        info = process.as_dict(attrs=("pid","name","username"))
        listprocess.append(info)
    os.mkdir(x)
    x=os.path.join(x,"Marvellous.txt")
    
    fobj=open(x,"w")
    for Data in listprocess :
    
        fobj.write("\n \n  PID is : %s"%Data.get("pid"))
        fobj.write("  Name is : %s"%Data.get("name"))
        fobj.write("  Username is : %s "%Data.get("username"))


    
def main():
    border="-"*50
    
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print(border)
            
            
            print("Help")
            print("This automation script is used for getting the info of process that are being executed on os ")
            print("For for more details type --u or --U")
            print("Thamk you ")
            print(border)
            

            return
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print(border)
            

            print("Usage")
            print("syntax for using the automation script is : ")
            print("python file_name Folder_Name")
            print("Folder_Name : It is used to create the folder in which the log files are created ")
            print("Thank you for using automation script")
            print(border)
            

        elif(os.path.exists(sys.argv[1])):
            print("Path already exists")
        elif(os.path.isdir(sys.argv[1])):
            print("Directory already exists ")
        else :
            display(sys.argv[1])
    else :
        print(border)

        print("Invalid No. og arguments")
        print("Please use --h of --u for halp or usage respectively ")
        print("Thank you for using automation script ")
        print(border)
        
    
if __name__=="__main__":
    main()